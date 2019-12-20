import { auth , authEpics} from "./auth";
//import { list , listEpics} from "./list";
import { combineReducers } from "redux";
import { combineEpics } from "redux-observable";

export const rootReducers = combineReducers({  auth });
export const rootEpics = combineEpics(
    authEpics.loginEpic,
    authEpics.registerEpic,/*
    authEpics.checkUserEpic,
    listEpics.listEpic,*/
    authEpics.logoutEpic,
);