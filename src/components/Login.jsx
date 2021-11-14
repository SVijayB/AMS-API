import React, { useEffect, useContext, useState } from "react";
import {
  Button,
  Grid,
  Paper,
  Avatar,
  TextField,
  Typography,
  Link
  
} from "@material-ui/core";
import VpnKeyOutlinedIcon from "@material-ui/icons/VpnKeyOutlined";


function Login() {
  const gridStyle = {
    width: "100%",
    height: "100vh",
    backgroundImage: `url("./4066549.jpg")`,
    position: "absolute",
  };
  const paperStyle = {
    padding: "20px",
    height: "70vh",
    width: 380,
    margin: "80px auto",
  };
  const avatarStyle = { backgroundColor: "red" };
  const textStyle = { padding: 20 };
  const buttonStyle = {
    marginTop: 40,
    backgroundColor: "red",
    color: "#fff",
    textAlign:"center"
  };
  const inputStyle = { marginTop: 20 };
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [login,setLogin]= useState(false);
  const submitcount = 0;

  

  async function handleSubmit(e) {
    e.preventDefault();
    const str=email.split("@");
    const mailid= str.pop();
    if(mailid  == "vitap@ac.in" && password !=""){
        setLogin(true)
    }else{
       setLogin(false)
    }
  }

  return (
    <>
    <Grid style={gridStyle}>
      <Paper elevation={10} style={paperStyle}>
        <Grid align="center">
          <Avatar style={avatarStyle}>
            <VpnKeyOutlinedIcon />
          </Avatar>
          <h2 style={textStyle}>Sign in</h2>
        </Grid>
        <form onSubmit={handleSubmit}>
          <TextField
            onChange={(e) => {setEmail(e.target.value)
            console.log(e.target.value);}}
            label="Email"
            placeholder="Email"
            fullWidth
            required
          />
          <TextField
            onChange={(e) => setPassword(e.target.value)}
            style={inputStyle}
            label="Password"
            placeholder="Password"
            type="password"
            fullWidth
            required
          />
          <Button
            style={buttonStyle}
            variant="contained"
            color="white"
            type="submit"
            align="center"
            fullWidth
          >
            Login
          </Button>
        </form>
        <Typography style={textStyle}>
          {" "}
          <Link href="/signup" color="secondary" style={textStyle}>
          Forget Password?
          </Link>
          <Link href="/signup" color="secondary" style={textStyle}>
          Sign up
          </Link>
        </Typography>
      </Paper>
    </Grid>
   
    </>
  );
}

export default Login;