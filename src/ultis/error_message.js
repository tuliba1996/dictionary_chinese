
const error_message =  {
  401: "Email or password is invalid",
  403: "You don't have permission",
  404: "Link not found",
  500: "Internal server error"
};

const get_error_message = (status) => {
  return error_message[status]
}

export default get_error_message;
