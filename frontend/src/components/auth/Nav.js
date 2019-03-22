import React from 'react';

function Nav(props) {
  const logged_out_nav = (
    <ul>
      <li onClick={() => props.display_form('login')}>Login</li>
      <li onClick={() => props.display_form('signup')}>Signup</li>
    </ul>
  );

  const logged_in_nav = (
    <ul>
      <li onClick={props.handle_logout}>Logout</li>
    </ul>
  );
  return <div>{props.logged_in ? logged_in_nav : logged_out_nav}</div>;
}

export default Nav;