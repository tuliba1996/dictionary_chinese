import axiosInstance from "./axios";
import get_error_message from "./error_message";
export default class FetchRequest {
  onSuccess(response) {
    if (
      response.status === 200 ||
      response.status === 201 ||
      response.status === 204
    ) {
      return {
        status: "ok",
        data: response.data,
      };
    }
  }

  onError(error) {
    if (error.response) {
      return {
        status: "error",
        message: get_error_message(error.response.status),
      };
    }
  }

  post(url, data) {
    return axiosInstance({
      method: "post",
      url: url,
      data: data,
    })
      .then(this.onSuccess)
      .catch(this.onError);
  }

  get(url, params) {
    return axiosInstance({
      method: "get",
      url: url,
      params: params,
    })
      .then(this.onSuccess)
      .catch(this.onError);
  }

  delete(url) {
    return axiosInstance({
      method: "delete",
      url: url,
    })
      .then(this.onSuccess)
      .catch(this.onError);
  }

  setAuthorizationHeader(token) {
    if (token !== "")
      axiosInstance.defaults.headers.common[
        "Authorization"
      ] = `Bearer ${token}`;
  }

  deleteAuthorizationHeader() {
    axiosInstance.defaults.headers.common["Authorization"] = "";
  }
}
