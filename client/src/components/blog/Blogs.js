import React, {useEffect, useContext}from 'react'
import { AppContext } from '../../context/AppContext';
import {gql, useQuery} from '@apollo/client'
import Blog from './Blog'

const GET_BLOGS = gql`
        query{
            blogs {
                edges{
                    node{
                        id
                        blogpic
                        title
                    }
                }
            }
        }
`;

const Blogs = () => {
    const { data } = useQuery(GET_BLOGS);
    const { blogs, setBlogs } = useContext(AppContext)
    useEffect(()=>{
       if(data) {
        setBlogs(data)
        console.log(blogs)
       }
       // eslint-disable-line react-hooks/exhaustive-deps
    }, [data])
    return (
            <div>
                <Blog />
            </div>
    )
}

export default Blogs