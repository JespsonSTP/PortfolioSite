import React from 'react'
import Navbar from '../components/navbar/Navbar'
import Jepy from '../components/showcase/Jepy.jpg'

const Showcase = ()=> {

    return (
        <div>
        <Navbar />
        <img src={Jepy} />
        <p>Hi, I'm Jespson Saint-Pierre, I Build Scalable Softwares</p>
        <form>
        <input></input>
        <input></input>
        </form>
        </div>
    )
}


export default Showcase
