import React, {Component} from 'react'
import Navbar from '../components/navbar/Navbar'
import Showcase from '../components/showcase/Showcase'
import Projects from '../components/projects/Projects'
class Home extends Component {
    render() {
      return (
        <div>
            <Navbar />
            <Showcase />
            <Projects />
        </div>
      )
    }
  }
  
  export default Home