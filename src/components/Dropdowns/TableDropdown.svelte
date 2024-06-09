<script>
  import { createPopper } from "@popperjs/core";

  let dropdownPopoverShow = false;

  let btnDropdownRef;
  let popoverDropdownRef;

  export let url = "";
  export let title = "";

  const toggleDropdown = (event) => {
    event.preventDefault();
    if (dropdownPopoverShow) {
      dropdownPopoverShow = false;
    } else {
      dropdownPopoverShow = true;
      createPopper(btnDropdownRef, popoverDropdownRef, {
        placement: "bottom-start",
      });
    }
  };
</script>

<div>
  <a
    class="text-blueGray-500 py-1 px-3"
    href="#"
    bind:this={btnDropdownRef}
    on:click={toggleDropdown}
  >
    <i class="fas fa-ellipsis-v"></i>
  </a>
  <div
    bind:this={popoverDropdownRef}
    class="bg-white text-base z-50 float-left py-2 list-none text-left rounded shadow-lg min-w-48 {dropdownPopoverShow
      ? 'block'
      : 'hidden'}"
  >
    <a
      href={url}
      class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
      style="text-align: center;"
    >
      Visit Website
    </a>
    <form method="POST">
      <div
        style="display: none;"
      >
        <input type="text" value="{title}" name="title" id="title">
      </div>
      <button
        type="submit"
        class="text-sm py-2 px-4 font-normal block w-full whitespace-nowrap bg-transparent text-blueGray-700"
        >View Summary</button
      >
    </form>
  </div>
</div>
