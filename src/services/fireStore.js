import db from "../ultis/firebase";

export const getItems = async (name) => {
  const res = await db.collection(name).get();
  return res.docs.map((doc) => {
    return { ...doc.data(), id: doc.id };
  });
};

export const addItem = async (name, payload) => {
  const res = await db.collection("users").add(payload);
  return res.id;
};
