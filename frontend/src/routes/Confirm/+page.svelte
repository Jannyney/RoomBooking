<script lang="ts">
    import {book_info} from "$lib/store";
</script>

<div class="background h-3/4 pt-10 pb-52" id="get_in_touch">
  <div id="form" class="pb-10 ">
    <p class="text-neutral text-5xl font-bold p-20 text-center">Successfully Booked</p>
      {$book_info?.day}
        {$book_info?.month}
      {$book_info?.year}
      {$book_info?.start_time}
      {$book_info?.end_time}
            <div class="card-actions justify-center">
              <a href="/Cancellation" class="btn btn-secondary">Cancel your booking</a>
                <a href="/" class="btn btn-secondary">Back to home</a>
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
