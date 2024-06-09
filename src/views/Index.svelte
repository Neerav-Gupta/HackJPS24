<script>
  import IndexNavbar from "components/Navbars/IndexNavbar.svelte";
  import Footer from "components/Footers/Footer.svelte";

  const patternVue = "/assets/img/pattern_svelte.png";
  const documentation = "/assets/img/documentation.png";
</script>

<IndexNavbar />
<section class="header relative pt-16 items-center flex h-screen max-h-860-px">
  <div class="container mx-auto items-center flex flex-wrap">
    <div class="w-full md:w-8/12 lg:w-6/12 xl:w-6/12 px-4">
      <div class="pt-32 sm:pt-0">
        <h2 class="font-semibold text-4xl text-blueGray-600">
          Researching just got easier!
        </h2>
        <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
          Scholar Scribe is an open source webite which helps researchers in
          finding the most accurate and best rescources for their search. Try it
          out below!
        </p>
        <form
          class="md:flex hidden flex-row flex-wrap items-center lg:ml-auto mr-3"
          method="POST"
        >
          <div
            style="margin-top: 40px; width: 70%; float: left; height:40px; margin-right:10px;"
            class="relative flex w-full flex-wrap items-stretch"
          >
            <span
              class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 pl-3 py-3"
            >
              <i class="fas fa-search"></i>
            </span>
            <input
              type="text"
              placeholder="Search anything here..."
              id="search"
              name="search"
              class="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-sm shadow outline-none focus:outline-none focus:ring w-full pl-10"
            />
          </div>

          <div class="mt-12" style="float: left; margin-top: none;">
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

<section class="mt-48 md:mt-40 pb-40 relative bg-blueGray-100">
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
      <div
        class="w-10/12 md:w-6/12 lg:w-4/12 px-12 md:px-4 mr-auto ml-auto -mt-32"
      >
        <div
          class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded-lg bg-red-400"
        >
          <!-- Change Image -->
          <img
            alt="..."
            src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80"
            class="w-full align-middle rounded-t-lg"
          />
          <blockquote class="relative p-8 mb-4">
            <svg
              preserveAspectRatio="none"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 583 95"
              class="absolute left-0 w-full block h-95-px -top-94-px"
            >
              <polygon
                points="-30,95 583,95 583,65"
                class="text-red-400 fill-current"
              ></polygon>
            </svg>
            <h4 class="text-xl font-bold text-white">Easy to use!</h4>
            <p class="text-md font-light mt-2 text-white">
              This simple and eye-catching website is user-friendly and easy to
              use! Simply enter a topic you want to research and you will be
              provided with more than enough results to help complete your
              research!
            </p>
          </blockquote>
        </div>
      </div>

      <div class="w-full md:w-6/12 px-4">
        <div class="flex flex-wrap">
          <div class="w-full md:w-6/12 px-4">
            <div class="relative flex flex-col mt-4">
              <div class="px-4 py-5 flex-auto">
                <div
                  class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                >
                  <i class="fas fa-sitemap"></i>
                </div>
                <h6 class="text-xl mb-1 font-semibold">Options</h6>
                <p class="mb-4 text-blueGray-500">
                  Get lots of options for your research paper - up to a hundred
                  sources!
                </p>
              </div>
            </div>
            <div class="relative flex flex-col min-w-0">
              <div class="px-4 py-5 flex-auto">
                <div
                  class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                >
                  <i class="fas fa-drafting-compass"></i>
                </div>
                <h6 class="text-xl mb-1 font-semibold">Credibility</h6>
                <p class="mb-4 text-blueGray-500">
                  We verify that all of our scources are credible and reliable
                  rescources!
                </p>
              </div>
            </div>
          </div>
          <div class="w-full md:w-6/12 px-4">
            <div class="relative flex flex-col min-w-0 mt-4">
              <div class="px-4 py-5 flex-auto">
                <div
                  class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                >
                  <i class="fas fa-newspaper"></i>
                </div>
                <h6 class="text-xl mb-1 font-semibold">Rating</h6>
                <p class="mb-4 text-blueGray-500">
                  We rate our scources to show how similar they are to your
                  desired topic so you are not reading through useless
                  information!
                </p>
              </div>
            </div>
            <div class="relative flex flex-col min-w-0">
              <div class="px-4 py-5 flex-auto">
                <div
                  class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-white"
                >
                  <i class="fas fa-file-alt"></i>
                </div>
                <h6 class="text-xl mb-1 font-semibold">Summary</h6>
                <p class="mb-4 text-blueGray-500">
                  We give you a quick to-the-point summary so that you don't
                  have to read the whole thing!
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="container mx-auto px-4 pb-32 pt-48">
  <div class="items-center flex flex-wrap">
    <div class="w-full md:w-5/12 ml-auto px-12 md:px-4">
      <div class="md:pr-12">
        <div
          class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
        >
          <i class="fas fa-file-alt text-xl"></i>
        </div>
        <h3 class="text-3xl font-semibold">Carefully Crafted Summaries</h3>
        <p class="mt-4 text-lg leading-relaxed text-blueGray-500">
          This website will provide accurate and well crafted summaries which
          will save you lots of time and energy. You will never have to read the
          whole article guaranteed!
        </p>
        <ul class="list-none mt-6">
          <li class="py-2">
            <div class="flex items-center">
              <div>
                <span
                  class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-50 mr-3"
                >
                  <i class="fas fa-fingerprint"></i>
                </span>
              </div>
              <div>
                <h4 class="text-blueGray-500">
                  Built by Researchers for Researchers
                </h4>
              </div>
            </div>
          </li>
          <li class="py-2">
            <div class="flex items-center">
              <div>
                <span
                  class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-50 mr-3"
                >
                  <i class="fab fa-html5"></i>
                </span>
              </div>
              <div>
                <h4 class="text-blueGray-500">
                  Never have to read the whole article
                </h4>
              </div>
            </div>
          </li>
          <li class="py-2">
            <div class="flex items-center">
              <div>
                <span
                  class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blueGray-500 bg-blueGray-50 mr-3"
                >
                  <i class="far fa-paper-plane"></i>
                </span>
              </div>
              <div>
                <h4 class="text-blueGray-500">Quick and easy</h4>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>

    <div class="w-full md:w-6/12 mr-auto px-4 pt-24 md:pt-0">
      <img
        alt="..."
        class="max-w-full rounded-lg shadow-xl"
        style="
            transform: scale(1) perspective(1040px) rotateY(-11deg)
              rotateX(2deg) rotate(2deg);
          "
        src={documentation}
      />
    </div>
  </div>
</div>
<section class="py-20 bg-blueGray-600 overflow-hidden">
  <div class="container mx-auto pb-64">
    <div class="flex flex-wrap justify-center">
      <div class="w-full md:w-5/12 px-12 md:px-4 ml-auto mr-auto md:mt-64">
        <div
          class="text-blueGray-500 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-white"
        >
          <i class="fas fa-code-branch text-xl"></i>
        </div>
        <h3 class="text-3xl mb-2 font-semibold leading-normal text-white">
          Uses AI to Generate Summaries
        </h3>
        <p
          class="text-lg font-light leading-relaxed mt-4 mb-4 text-blueGray-400"
        >
          Get the context of the article in just a few quick sentences! We use
          AI powered text summarization!
        </p>
        <p
          class="text-lg font-light leading-relaxed mt-0 mb-4 text-blueGray-400"
        >
          Give it a shot now!
        </p>
      </div>

      <div class="w-full md:w-4/12 px-4 mr-auto ml-auto mt-32 relative">
        <i
          class="fab fa-github text-blueGray-700 text-55 absolute -top-150-px -right-100 left-auto opacity-80"
        ></i>
      </div>
    </div>
  </div>
</section>
<Footer />
