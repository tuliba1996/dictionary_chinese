import { request } from "./request";

export async function postLogin(form) {
  return await request.post("/token/", form);
}
