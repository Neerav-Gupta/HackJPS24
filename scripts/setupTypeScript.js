// @ts-check

const fs = require("fs");
const path = require("path");
const { argv } = require("process");

const projectRoot = argv[2] || path.join(__dirname, "..");

const packageJSON = JSON.parse(
  fs.readFileSync(path.join(projectRoot, "package.json"), "utf8")
);
packageJSON.devDependencies = Object.assign(packageJSON.devDependencies, {
  "svelte-check": "^1.2.5",
  "svelte-preprocess": "^4.6.9",
  "@rollup/plugin-typescript": "^8.2.0",
  typescript: "^4.2.3",
  tslib: "^2.1.0",
  "@tsconfig/svelte": "^1.0.10",
});

packageJSON.scripts = Object.assign(packageJSON.scripts, {
  validate: "svelte-check",
});

fs.writeFileSync(
  path.join(projectRoot, "package.json"),
  JSON.stringify(packageJSON, null, "  ")
);

const beforeMainJSPath = path.join(projectRoot, "src", "main.js");
const afterMainTSPath = path.join(projectRoot, "src", "main.ts");
fs.renameSync(beforeMainJSPath, afterMainTSPath);

const appSveltePath = path.join(projectRoot, "src", "App.svelte");
let appFile = fs.readFileSync(appSveltePath, "utf8");
appFile = appFile.replace("<script>", '<script lang="ts">');
appFile = appFile.replace("export let name;", "export let name: string;");
fs.writeFileSync(appSveltePath, appFile);

const rollupConfigPath = path.join(projectRoot, "rollup.config.js");
let rollupConfig = fs.readFileSync(rollupConfigPath, "utf8");

rollupConfig = rollupConfig.replace(
  `'rollup-plugin-terser';`,
  `'rollup-plugin-terser';
import sveltePreprocess from 'svelte-preprocess';
import typescript from '@rollup/plugin-typescript';`
);

rollupConfig = rollupConfig.replace(`'src/main.js'`, `'src/main.ts'`);

let foundCSS = false;
let match;

const configEditor = new RegExp(/css:.|\n*}/gim);
while ((match = configEditor.exec(rollupConfig)) != null) {
  if (foundCSS) {
    const endOfCSSIndex = match.index + 1;
    rollupConfig =
      rollupConfig.slice(0, endOfCSSIndex) +
      ",\n			preprocess: sveltePreprocess()," +
      rollupConfig.slice(endOfCSSIndex);
    break;
  }
  if (match[0].includes("css:")) foundCSS = true;
}

rollupConfig = rollupConfig.replace(
  "commonjs(),",
  "commonjs(),\n\t\ttypescript({ sourceMap: !production }),"
);
fs.writeFileSync(rollupConfigPath, rollupConfig);

const tsconfig = `{
  "extends": "@tsconfig/svelte/tsconfig.json",

  "include": ["src/**/*"],
  "exclude": ["node_modules/*", "__sapper__/*", "public/*"],
}`;
const tsconfigPath = path.join(projectRoot, "tsconfig.json");
fs.writeFileSync(tsconfigPath, tsconfig);

if (!argv[2]) {
  fs.unlinkSync(path.join(__filename));

  const remainingFiles = fs.readdirSync(path.join(__dirname));
  if (remainingFiles.length === 1 && remainingFiles[0] === ".DS_store") {
    fs.unlinkSync(path.join(__dirname, ".DS_store"));
  }

  if (fs.readdirSync(path.join(__dirname)).length === 0) {
    fs.rmdirSync(path.join(__dirname));
  }
}

fs.mkdirSync(path.join(projectRoot, ".vscode"));
fs.writeFileSync(
  path.join(projectRoot, ".vscode", "extensions.json"),
  `{
  "recommendations": ["svelte.svelte-vscode"]
}
`
);

console.log("Converted to TypeScript.");

if (fs.existsSync(path.join(projectRoot, "node_modules"))) {
  console.log(
    "\nYou will need to re-run your dependency manager to get started."
  );
}
