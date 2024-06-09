<script>
  // core components
  import IndexNavbar from "components/Navbars/IndexNavbar.svelte";
  import Footer from "components/Footers/Footer.svelte";
  import { onMount } from "svelte";
  let title = "";
  let link = "";
  let summary = [];
  let message = "";

  onMount(async () => {
    message = decodeURI(window.location.href.split("summary/")[1]);
    let res = await fetch(`./query?search=${message}`);
    let msg = await res.text();
    if (res.ok) {
      msg = JSON.parse(msg);
      title = msg[0];
      link = msg[1];
      summary = msg[3];
    }
  });
</script>

<div>
  <IndexNavbar />
  <main class="profile-page">
    <section class="relative block h-500-px">
      <div
        class="absolute top-0 w-full h-full bg-center bg-cover"
        style="
          background-image: url(https://images.unsplash.com/photo-1499336315816-097655dcfbda?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2710&q=80);
        "
      >
        <span
          id="blackOverlay"
          class="w-full h-full absolute opacity-50 bg-black"
        ></span>
      </div>
      <div
        class="top-auto bottom-0 left-0 right-0 w-full absolute pointer-events-none overflow-hidden h-70-px"
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
            class="text-blueGray-200 fill-current"
            points="2560 0 2560 100 0 100"
          ></polygon>
        </svg>
      </div>
    </section>
    <section class="relative py-16 bg-blueGray-200">
      <div class="container mx-auto px-4">
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-xl rounded-lg -mt-64"
        >
          <div class="px-6">
            <div class="flex flex-wrap justify-center">
              <div
                class="w-full lg:w-8/12 px-4 lg:order-3 lg:text-right lg:self-center"
              >
                <div class="text-center mt-12">
                  <h3
                    class="text-4xl font-semibold leading-normal mb-2 text-blueGray-700 mb-2"
                  >
                    {#if title == ""}
                      Loading...
                    {:else}
                      {title}
                    {/if}
                  </h3>
                </div>
                <div
                  class="mt-10 py-10 border-t border-blueGray-200 text-center"
                >
                  <div class="flex flex-wrap justify-center">
                    {#if summary == []}
                      <p class="mb-4 text-lg leading-relaxed text-blueGray-700">
                        Loading...
                      </p>
                    {:else}
                      {#each summary as section}
                        <p
                          class="mb-4 text-xl leading-relaxed text-blueGray-700"
                        >
                          {section[0]}
                        </p>
                        <p
                          class="mb-4 text-lg leading-relaxed text-blueGray-700"
                        >
                          {#each section[1] as bullet}
                            <p
                              class="mb-4 text-lg leading-relaxed text-blueGray-700"
                            >
                              {bullet}
                            </p>
                          {/each}
                        </p>{/each}
                    {/if}
                    <a href={link} class="font-normal text-red-500">
                      Visit Site
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
  <Footer />
</div>
