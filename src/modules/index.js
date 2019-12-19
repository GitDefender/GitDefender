import {notes, notesEpics} from "./notes";
import {auth, authEpics} from "./auth";
import {combineReducers} from "redux";
import {combineEpics} from "redux-observable";

export const rootReducers = combineReducers({notes, auth});
export const rootEpics = combineEpics(
    notesEpics.addNoteEpic,
    authEpics.loginEpic,
    authEpics.registerEpic
);