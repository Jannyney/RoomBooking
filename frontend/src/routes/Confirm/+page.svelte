<script lang="ts">
    import {book_info} from "$lib/store";
    import {logged_in} from "$lib/store";
</script>

<div class="background h-3/4 pt-5 " id="get_in_touch">
  <div id="form" class="pb-10 ">
    <p class="text-neutral text-5xl font-bold p-10 text-center">Successfully Booked</p>

    <div class="card w-96 bg-base-100 shadow-xl">
  <div class="card-body">
    <h2 class="card-title self-center pb-5">Booking Information</h2>
    <p>Booking ID: </p>
    <p>Name: </p>
    <p>Room: </p>
    <p>Date: {$book_info?.day}
        {$book_info?.month}
      {$book_info?.year}
      </p>
    <p>Time:
      {$book_info?.start_time}-
      {$book_info?.end_time}</p>
    <div class="card-actions justify-center pt-5">
            <a href="/Cancellation" class="btn btn-secondary">Cancel booking</a>
       {#if ($logged_in?.username==="admin")}
       <a href="/AdminBookHistory" class="btn btn-secondary">View History</a>
         {:else }
 <a href="/UserBookHistory" class="btn btn-secondary">View History</a>
         {/if}

    </div>
  </div>
</div>


  </div>
</div>

<style>
  .background{
    background-color: rgb(255,217,222);
  }
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
