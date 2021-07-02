import { request } from "./request";

export async function postRegister(form) {
  return await request.post("/user/", form);
}
