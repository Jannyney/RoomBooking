<script lang="ts">
	import type { PageData } from './$types';
    import { onMount } from 'svelte';
    import {logged_in} from "$lib/store";
    import { goto } from "$app/navigation";
    import {book_info} from "$lib/store";
	export let data: PageData;
    onMount(()=> {
        if (!$logged_in){
            goto("/SignIn");
        }
    })
    let day = 1;
    let month = "January";
    let year = 2023;
    let start_time = "8:00";
    let end_time = "9:00";
    const times = ["8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"];
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    function save_info(){
        book_info.set({
            day : day,
            month: month,
            year: year,
            start_time: start_time,
            end_time: end_time
        })
         goto("/Confirm")
    }

</script>
        <p class="text-content text-5xl font-bold pb-16 text-center">Edit Room</p>
<div class="flex flex-row pb-16">
    { #if data.post}
        <div class="w-2/3 flex flex-col ">
            <img style="width: 60%; display: block; margin-left: auto; margin-right: auto;" src="{data.post.image}" alt="Room Image">
        </div>
        <div>
            <h1 class="font-bold text-3xl text-center py-2">{data?.post.title}</h1>
            <p class=" py-5 text-xl">New Room Name</p>
            <input type="text" placeholder={data?.post.title} class="input input-bordered w-full max-w-xs" />

            <p class=" py-5 text-xl">Room Type</p>
            <select bind:value={day} class="select select-bordered  max-w-xs">
                {#each [...Array(31).keys()] as day}
              <option>{day+1}</option>
                {/each} </select>

            <p class=" py-5 text-xl">New Room Picture Path</p>
            <input type="text" placeholder="https://" class="input input-bordered w-full max-w-xs" />

             <div class="card-actions justify-center py-8">
              <button on:click={save_info} class="btn btn-primary ">Submit</button>
       </div>
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
