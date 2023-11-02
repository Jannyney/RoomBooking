<script lang="ts">
	import type { PageData } from './$types';
    import { onMount } from 'svelte';
    import {logged_in} from "$lib/store";
    import { goto } from "$app/navigation";
	export let data: PageData;
    onMount(()=> {
        if (!$logged_in){
            goto("/SignIn");
        }
    })
</script>
        <p class="text-neutral text-5xl font-bold pb-10 text-center">Reservation</p>
<div class="flex flex-col">
    { #if data.post}
        <div><img style="width: 30%; display: block; margin-left: auto; margin-right: auto;" src="{data.post.image}" alt="Room Image"></div>
        <div>
            <h1 class="font-bold text-2xl text-center py-10">{data?.post.title}</h1>
            </div>
        <div class="mb-6 flex justify-center">
        <div class="dropdown">
          <label tabindex="0" class="btn m-1">Select Start Time</label>
              <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
                <li><a>8:00</a></li>
                <li><a>9:00</a></li>
                  <li><a>10:00</a></li>
                <li><a>11:00</a></li>
                   <li><a>12:00</a></li>
                <li><a>13:00</a></li>
                   <li><a>14:00</a></li>
                <li><a>15:00</a></li>
                   <li><a>16:00</a></li>
              </ul>
        </div>

                <div class="dropdown">
          <label tabindex="0" class="btn m-1">Select End Time</label>
          <ul tabindex="0" class="dropdown-content z-[1] menu p-2 shadow bg-base-100 rounded-box w-52">
            <li><a>9:00</a></li>
              <li><a>10:00</a></li>
            <li><a>11:00</a></li>
               <li><a>12:00</a></li>
            <li><a>13:00</a></li>
               <li><a>14:00</a></li>
            <li><a>15:00</a></li>
               <li><a>17:00</a></li>
          </ul>
        </div>
        </div>
       <div class="card-actions justify-center">
              <a href="/Confirm" class="btn btn-primary">Book Now</a>
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
