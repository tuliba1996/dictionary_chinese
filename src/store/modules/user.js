import Storage from "../../ultis/storage";
import { request } from "../../services/request";

export const userStorage = new Storage("user");

export const checkAuthorization = (user) => {
  return user !== null;
};

const state = {
  user: userStorage.get(),
};

const actions = {
  onUpdateUser({ commit }, payload) {
    commit("updateUser", payload);
  },
};

const mutations = {
  updateUser(state, userData) {
    if (userData === undefined || userData === null) {
      userStorage.remove();
      request.deleteAuthorizationHeader();
      state.user = null;
    } else {
      userStorage.set(userData);
      request.setAuthorizationHeader(userData.access);
      state.user = userData;
    }
  },
};

const getters = {
  user(state) {
    return state.user;
  },
  user_id(state) {
    return state.user?.id;
  },
  isAuthorized(state) {
    return checkAuthorization(state.user);
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
