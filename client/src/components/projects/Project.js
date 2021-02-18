import React, {Component} from 'react'

class Project extends Component {
    state = {
        projectname : 'HomeCookin',
        projectPicture : 'the picture',
        projectDescription : 'this is an amazing App'
    }
    render() {
        const {projectname, projectPicture, projectDescription } = this.state
        return (
            <div className='card-wrapper'>
            <div className="card">
            <img/>
            <h1>projectname</h1>
            <p>projectDescription</p>
            </div>
            </div>
        )
    }
}

export default Project