import {writable} from "svelte/store";

export let logged_in = writable(null)

export let signed_up = writable(null)

export let book_info = writable(null)
