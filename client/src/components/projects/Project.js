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
            <div>
            </div>
        )
    }
}

export default Project