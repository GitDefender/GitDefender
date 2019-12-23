const endpoint = "ENDPOINT URL"

const get_repository = endpoint + "/get_repository"
const get_commit = endpoint + "/get_commit"
const get_branch = endpoint + "/get_branch"
const get_code_detect = endpoint + "/get_code_detect"

const auth_login = endpoint + "/auth/login"
const auth_logout = endpoint + "/auth/logout"
const auth_register = endpoint + "/auth/register"
const auth_user = endpoint + "/auth/user"

const auth_oauth2 = endpoint + "/auth/user"

export {
    get_repository, get_code_detect, get_commit, auth_login, auth_logout,
    auth_oauth2, auth_register, auth_user
};