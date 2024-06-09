<!-- App.svelte -->
<script>
  import { Router, Route } from "svelte-routing";
  import Index from "./views/Index.svelte";
  import Summary from "./views/Summary.svelte";
  import Search from "./views/Search.svelte"

  export let url = "";
</script>

<Router url="{url}">
  <Route path="search/summary/*any" component="{Summary}" />
  <Route path="search/*search" component="{Search}" />
  <Route path="" component="{Index}" />
</Router>
