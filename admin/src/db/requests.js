
import axios from "axios";

// const baseUrl = process.env.VUE_APP_BASE_URL;

export class DBrequests {
  
    // static baseUrl;

    constructor() {
        this.baseUrl = process.env.VUE_APP_BASE_URL;
    }

    async fetch(url) {
        console.log('BAseURL: ',this.baseUrl);
        const response = await axios.get(this.baseUrl + url);
        
        return response.data;
    }

    async create(url, data) {
        const response = await axios.post(this.baseUrl + url, data);
        return response.data;
    }

    async update(url, data) {
        const response = await axios.put(this.baseUrl + url, data);
        return response.data;
    }

    async delete(url) {
        const response = await axios.delete(this.baseUrl + url);
        return response.data;
    }



}

export const DBrequestsObj = new DBrequests();



