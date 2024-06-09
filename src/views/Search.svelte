<script>
  import IndexNavbar from "components/Navbars/IndexNavbar.svelte";
  import Footer from "components/Footers/Footer.svelte";
  import CardTable from "../components/Cards/CardTable.svelte";
  import { onMount } from "svelte";

  const patternVue = "/assets/img/pattern_svelte.png";

  let data = [];
  let message = "";

  onMount(async () => {
    message = decodeURI(window.location.href.split("search/")[1]);
    let res = await fetch(`./query?search=${message}`);
    let msg = await res.text();
    if (res.ok) {
      data = JSON.parse(msg);
      console.log(data);
    }
  });
</script>

<IndexNavbar />
<section class="header relative pt-16 items-center flex h-screen max-h-860-px">
  <div class="container mx-auto items-center flex flex-wrap">
    <div class="w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4">
      <div class="pt-32 sm:pt-0">
        <h2 class="font-semibold text-4xl text-blueGray-600">
          Search a topic!
        </h2>
        <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
          Get summaries and texts now!
        </p>
        <form
          class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"
          method="POST"
        >
          <div
            style="margin-top: 10px; width: 70%; float: left; height:40px; margin-right:10px;"
            class="relative flex w-full flex-wrap items-stretch"
          >
            <span
              class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
            >
              <i class="fas fa-search"></i>
            </span>
            <input
              type="text"
              placeholder={message}
              id="search"
              name="search"
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:ring w-full pl-10"
            />
          </div>

          <div class="mt-5" style="float: left; margin-top: none;">
            <!-- svelte-ignore a11y-missing-attribute -->
            <!-- svelte-ignore a11y-click-events-have-key-events -->
            <button
              type="submit"
              method="POST"
              class="github-star ml-1 text-white font-bold px-4 py-3 rounded outline-none focus:outline-none mr-1 mb-1 bg-blueGray-700 active:bg-blueGray-600 uppercase text-sm shadow hover:shadow-lg ease-linear transition-all duration-150"
              target="_blank"
            >
              <i class="fas fa-search"></i>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- Change Image -->
  <img
    class="absolute top-0 b-auto right-0 pt-16 sm:w-6/12 -mt-48 sm:mt-0 w-10/12 max-h-860-px"
    src={patternVue}
    alt="..."
  />
</section>

<section class="mt-40 md:mt-40 pb-20 pt-20 relative bg-blueGray-100">
  <div
    class="-mt-20 top-0 bottom-auto left-0 right-0 w-full absolute h-20"
    style="transform: translateZ(0);"
  >
    <svg
      class="absolute bottom-0 overflow-hidden"
      xmlns="http://www.w3.org/2000/svg"
      preserveAspectRatio="none"
      version="1.1"
      viewBox="0 0 2560 100"
      x="0"
      y="0"
    >
      <polygon
        class="text-blueGray-100 fill-current"
        points="2560 0 2560 100 0 100"
      ></polygon>
    </svg>
  </div>
  <div class="container mx-auto">
    <div class="flex flex-wrap items-center">
      {#if data.length == 0 || message == ""}
      <h2 class="font-semibold text-2xl text-blueGray-600">
        Generating results! Almost there...
      </h2>
      {:else}
        <CardTable {data} topic={message} />
      {/if}
    </div>
  </div>
</section>
<Footer />

<style>
</style>
