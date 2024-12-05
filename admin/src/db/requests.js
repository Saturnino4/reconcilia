
import axios from "axios";

export class DBrequests {
  
    static baseUrl;

    constructor() {
        this.baseUrl = process.env.VUE_APP_BASE_URL;
    }

    async fetch(url) {
        const response = await axios.get(this.baseUrl + url);
        console.log('BAseURL: ',this.baseUrl);
        
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



