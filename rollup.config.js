import svelte from "rollup-plugin-svelte";
import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import livereload from "rollup-plugin-livereload";
import { terser } from "rollup-plugin-terser";
import alias from "@rollup/plugin-alias";

const production = !process.env.ROLLUP_WATCH;

const aliases = alias({
  resolve: [".svelte", ".js"],
  entries: [
    { find: "components", replacement: "src/components" },
    { find: "views", replacement: "src/views" },
    { find: "assets", replacement: "src/assets" },
  ],
});

function serve() {
  let server;

  function toExit() {
    if (server) server.kill(0);
  }

  return {
    writeBundle() {
      if (server) return;
      server = require("child_process").spawn(
        "npm",
        ["run", "start", "--", "--dev"],
        {
          stdio: ["ignore", "inherit", "inherit"],
          shell: true,
        }
      );

      process.on("SIGTERM", toExit);
      process.on("exit", toExit);
    },
  };
}

export default {
  input: "src/main.js",
  output: {
    sourcemap: true,
    format: "iife",
    name: "app",
    file: "public/build/bundle.js",
  },
  plugins: [
    svelte({
      dev: !production,
      css: (css) => {
        css.write("bundle.css");
      },
    }),
    resolve({
      browser: true,
      dedupe: ["svelte"],
    }),
    commonjs(),

    !production && serve(),

    !production && livereload("public"),

    production && terser(),

    aliases,
  ],
  watch: {
    clearScreen: false,
  },
};
