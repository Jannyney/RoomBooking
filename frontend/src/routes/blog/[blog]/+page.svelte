<script lang="ts">
	import type { PageData } from './$types';
	export let data: PageData;
</script>
        <p class="text-neutral text-5xl font-bold pb-10 text-center">Reservation</p>
<div class="flex flex-col">
    { #if data.post}
        <div><img style="width: 30%; display: block; margin-left: auto; margin-right: auto;" src="{data.post.image}" alt="Room Image"></div>
        <div>
            <h1 class="font-bold text-3xl text-center py-10">{data?.post.title}</h1>
            <div class="text-center text-justify px-56 pt-10 pb-20 text-xl" style="white-space: pre-wrap">{ data?.post.content}</div>
            </div>
        {/if}
</div>
<style>

  /*extra small*/
  @media (min-width: 110px) {
    #form {
      margin-left: 1rem;
      margin-right: 1rem;
    }
  }
  /*small*/
  @media (min-width: 640px) {
    #form {
      margin-left: 2.5rem;
      margin-right: 2.5rem;
    }
  }
  /*medium*/
  @media (min-width: 768px){
    #form {
      margin-left: 10rem;
      margin-right: 10rem;
    }
  }
  /*large*/
  @media (min-width: 1024px) {
    #form {
      margin-left: 20rem;
      margin-right: 20rem;
    }
  }
  /*large*/
  @media (min-width: 1536px) {
    #form {
      margin-left: 35rem;
      margin-right: 35rem;
    }
  }
  /*#form {*/
  /*  margin-left: 35rem;*/
  /*  margin-right: 35rem;*/
  /*}*/
</style>
