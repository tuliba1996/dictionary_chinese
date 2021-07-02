import axios from "axios";
// import { CONFIG } from "../config";

const axiosInstance = axios.create({
  baseURL: `/api`,
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
  },
});

export default axiosInstance;
