import { request } from "./request";
import { addItem } from "./fireStore";

export async function getTopic(query) {
  return await request.get("/topic/", query);
}

export async function postTopic(data) {
  return await request.post("/topic/", data);
}

export async function deleteTopic(data) {
  return await request.delete(`/topic/${data}`);
}

export async function addTopic(data) {
  return await addItem("topic", data);
}
