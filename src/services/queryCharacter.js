import { request } from "./request";

export async function queryCharacter(q) {
  return await request.get("/character/", { search: q });
}
