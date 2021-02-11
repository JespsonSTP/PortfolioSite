import React, {useEffect, useContext}from 'react'
import { AppContext } from '../../context/AppContext';
import {gql, useQuery} from '@apollo/client'
import Project from './Project'

const GET_PROJECTS = gql`
                      query{
                        projects {
                          edges{
                            node{
                              id
                              projectname
                              textDescription
                            }
                          }
                        }
                      }
                    `;

const Projects = () => {
    const { data } = useQuery(GET_PROJECTS);
    const { projects, setProjects } = useContext(AppContext)
    useEffect(()=>{
       if(data) {
        setProjects(data)
        console.log(projects)
       }
       // eslint-disable-line react-hooks/exhaustive-deps
    }, [data])
    return (
            <div>
                <Project/>
            </div>
    )
}

export default Projects
