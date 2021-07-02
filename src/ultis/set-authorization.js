import { request } from "../services/request";
import { userStorage } from "../store/modules/user";

export default function () {
  const token = userStorage.get()?.access;
  if (token !== undefined) request.setAuthorizationHeader(token);
}
