import axios from "axios";

export class DBrequests {
    constructor() {
        this.baseUrl = process.env.VUE_APP_BASE_URL;
        this.api = axios.create({
            baseURL: this.baseUrl,
            headers: {
                'Content-Type': 'application/json',
                // Adicione outros headers necessários aqui
            }
        });
    }

    async fetch(url) {
        try {
            console.log('BaseURL:', this.baseUrl);
            const response = await this.api.get(url);
            return response.data;
        } catch (error) {
            console.error(`Erro ao buscar dados de ${url}:`, error);
            throw error;
        }
    }

    async create(url, data) {
        try {
            const response = await this.api.post(url, data);
            return response.data;
        } catch (error) {
            console.error(`Erro ao criar dados em ${url}:`, error);
            throw error;
        }
    }

    async update(url, data) {
        try {
            const response = await this.api.put(url, data);
            return response.data;
        } catch (error) {
            console.error(`Erro ao atualizar dados em ${url}:`, error);
            throw error;
        }
    }

    async deleteItem(url) { // Renomeado para evitar conflito com palavra reservada
        try {
            const response = await this.api.delete(url);
            return response.data;
        } catch (error) {
            console.error(`Erro ao deletar dados em ${url}:`, error);
            throw error;
        }
    }
}

export const DBrequestsObj = new DBrequests();