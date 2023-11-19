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
        <p class="text-content text-5xl font-bold pb-5 text-center">Reservation</p>
<div class="flex flex-col">
    { #if data.post}
        <div><img style="width: 30%; display: block; margin-left: auto; margin-right: auto;" src="{data.post.image}" alt="Room Image"></div>
        <div>
            <h1 class="font-bold text-2xl text-center py-5">{data?.post.title}</h1>
            </div>

        <div class="mb-6 flex flex-col ">
             {#if ($logged_in?.username==="admin")}
                  <div class="flex justify-center pb-5">Select Username</div>
                  <div class="flex justify-center"><select bind:value={day} class="select select-bordered  max-w-xs">
                {#each [...Array(31).keys()] as day}
              <option>{day+1}</option>
                {/each} </select></div>

             {/if}

            <div class="flex justify-center py-5 ">Select date</div>
            <div class="flex justify-center"><select bind:value={day} class="select select-bordered  max-w-xs">
                {#each [...Array(31).keys()] as day}
              <option>{day+1}</option>
                {/each}
            </select>

            <select bind:value={month} class="select select-bordered  max-w-xs">
              {#each months as month}
              <option>{month}</option>
                {/each}
            </select>

             <select bind:value={year} class="select select-bordered  max-w-xs">
              <option>{2023}</option>
            </select>
        </div></div>


        <div class="mb-6 flex flex-col justify-center">
           <div class="flex justify-center pb-5">Select Time</div>
            <div class="flex justify-center"><select bind:value={start_time} class="select select-bordered  max-w-xs">
                {#each times as time}
              <option>{time}</option>
                {/each}
            </select>

            <select bind:value={end_time} class="select select-bordered  max-w-xs">
              {#each times as time}
              <option>{time}</option>
                {/each}
            </select>
        </div></div>
       <div class="card-actions justify-center pb-5">
              <button on:click={save_info} class="btn btn-primary">Book Now</button>
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
