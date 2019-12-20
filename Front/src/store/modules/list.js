import axios from "axios";
/*
const OAUTH = "list/OAUTH";


export const oauth = () => ({
    type: OAUTH
});

const listEpic = (action$, state$) => {
    return axios.get({
        url: 'http://test.gitdefender.com:8080/api/v1/auth/oauth2"',
        header: {
            token: localStorage.getItem("token")
        }
    })
        .then(function (response) {
            console.log("handleClickTestSuccess");
            console.log(response);
        })
        .catch(function (error) {
                console.log("handleClickTestFail");
                console.log(error);
            }
        );
};

const initialState = {
    logged: false,
    token: null
};

export const list = (state = initialState, action) => {
    return {
        ...state,
        logged: true,
    }
};

export const listEpics = {listEpic};*/