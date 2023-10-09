import React from 'react'

function Login() {
  return (
    <div>
      <form>
        <p><input type="text" name="email" id="email" /></p>
        <p><input type="text" name="password" id="password" /></p>
        <input type="submit" value="Se connecter" />
      </form>
    </div>
  )
}

export default Login