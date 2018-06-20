import { bubble  as Menu } from 'react-burger-menu'
import React from 'react';
import '../css/SideBar.css'
export default class SideBar extends React.Component {
  showSettings (event) {
    event.preventDefault();
  }

  render () {
    return (
      <Menu  noOverlay className='small-button' customBurgerIcon={<img src="https://fancomicbiblios.files.wordpress.com/2014/08/calendar.png?w=816&h=9999"/>} customCrossIcon={ <img src="https://cdn3.iconfinder.com/data/icons/interface/100/close_button-128.png" /> }>
        <img src ="https://cdn3.iconfinder.com/data/icons/medcare/512/Stethoscope-256.png" align="middle" alt="Icone" />
        <li><a href="/DoctorForm"><span className="sub_icon glyphicon glyphicon-plus"></span>  Cadastrar médico</a></li>
        <li><a href="/ScheduleTable"><span className="sub_icon glyphicon glyphicon-calendar "></span>  Visualizar tabela</a></li>
      </Menu>
    );
  }
}
