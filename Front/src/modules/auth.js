import {ajax} from "rxjs/observable/dom/ajax";
import {of} from "rxjs";
import {map, mergeMap, catchError, withLatestFrom} from "rxjs/operators";
import {ofType} from "redux-observable";

const INITIALIZE_INPUT = "auth/INITIALIZE_INPUT";

const REGISTER = "auth/REGISTER";
const REGISTER_SUCCESS = "auth/REGISTER_SUCCESS";
const REGISTER_FAILURE = "auth/REGISTER_FAILURE";

const LOGIN = "auth/LOGIN";
const LOGIN_SUCCESS = "auth/LOGIN_SUCCESS";
const LOGIN_FAILURE = "auth/LOGIN_FAILURE";

const INITIALIZE_ERROR = "auth/INITIALIZE_ERROR";

const CHANGE_INPUT = "auth/CHANGE_INPUT";

export const initializeInput = () => ({
    type: INITIALIZE_INPUT
});
export const register = () => ({
    type: REGISTER
});

export const registerSuccess = ({user, token}) => ({
    type: REGISTER_SUCCESS,
    payload: {
        user,
        token
    }
});

export const registerFailure = error => ({
    type: REGISTER_FAILURE,
    payload: {
        error
    }
});

export const login = () => ({
    type: LOGIN
});

export const loginSuccess = ({user, token}) => ({
    type: LOGIN_SUCCESS,
    payload: {
        user,
        token
    }
});

export const loginFailure = error => ({
    type: LOGIN_FAILURE,
    payload: {
        error
    }
});


export const initializeError = () => ({
    type: INITIALIZE_ERROR
});

const registerEpic = (action$, state$) => {
    return action$.pipe(
        ofType(REGISTER),
        withLatestFrom(state$),
        mergeMap(([action, state]) => {
            const {username, password} = state.auth.form;
            return ajax.post(`/api/auth/register/`, {username, password}).pipe(
                map(response => {
                    const {user, token} = response.response;
                    return registerSuccess({user, token});
                }),
                catchError(error =>
                    of({
                        type: REGISTER_FAILURE,
                        payload: error,
                        error: true
                    })
                )
            );
        })
    );
};

const loginEpic = (action$, state$) => {
    return action$.pipe(
        ofType(LOGIN),
        withLatestFrom(state$),
        mergeMap(([action, state]) => {
            const {username, password} = state.auth.form;
            return ajax.post(`/api/auth/login/`, {username, password}).pipe(
                map(response => {
                    const {user, token} = response.response;
                    return loginSuccess({user, token});
                }),
                catchError(error =>
                    of({
                        type: LOGIN_FAILURE,
                        payload: error,
                        error: true
                    })
                )
            );
        })
    );
};
const initialState = {
    form: {
        username: "",
        password: ""
    },
    error: {
        triggered: false,
        message: ""
    },
    logged: false,
    userInfo: {
        id: null,
        username: "",
        token: null
    }
};

export const auth = (state = initialState, action) => {
    switch (action.type) {
        case INITIALIZE_INPUT:
            return {
                ...state,
                form: {
                    username: "",
                    password: ""
                }
            };
        case CHANGE_INPUT:
            let newForm = state.form;
            newForm[action.payload.name] = action.payload.value;
            return {
                ...state,
                form: newForm
            };
        case INITIALIZE_ERROR:
            return {
                ...state,
                error: {
                    triggered: false,
                    message: ""
                }
            };
        case REGISTER_SUCCESS:
            return {
                ...state,
                logged: true,
                userInfo: {
                    id: action.payload.user.id,
                    username: action.payload.user.username,
                    token: action.payload.token
                }
            };
        case REGISTER_FAILURE:
            switch (action.payload.status) {
                case 400:
                    return {
                        ...state,
                        error: {
                            triggered: true,
                            message: "WRONG USERNAME OR PASSWORD"
                        }
                    };
                case 500:
                    return {
                        ...state,
                        error: {
                            triggered: true,
                            message: "TOO SHORT USERNAME OR PASSWORD"
                        }
                    };
                default:
                    return {
                        ...state
                    };
            }
        case LOGIN_SUCCESS:
            return {
                ...state,
                logged: true,
                userInfo: {
                    id: action.payload.user.id,
                    username: action.payload.user.username,
                    token: action.payload.token
                }
            };
        case LOGIN_FAILURE:
            switch (action.payload.status) {
                case 400:
                    return {
                        ...state,
                        error: {
                            triggered: true,
                            message: "WRONG USERNAME OR PASSWORD"
                        }
                    };
                case 500:
                    return {
                        ...state,
                        error: {
                            triggered: true,
                            message: "PLEASE TRY AGAIN"
                        }
                    };
                default:
                    return {
                        ...state
                    };
            }

        default:
            return state;
    }
};

export const changeInput = ({name, value}) => ({
    type: CHANGE_INPUT,
    payload: {
        name,
        value
    }
});