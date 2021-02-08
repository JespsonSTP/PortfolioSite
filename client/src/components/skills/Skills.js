import React from 'react'
import {
    FaReact,
    FaPython,
    FaHtml5,
    FaCss3Alt,
    FaGitAlt,
    FaDocker,
    FaGitlab,
    FaJenkins,
    FaJava,
    FaNode
  } from "react-icons/fa";
import { SiStyledComponents, SiFlask, SiJavascript, SiDjango, SiKubernetes, SiSpring, SiGraphql} from "react-icons/si";
  
const Skills = ()=> {

    return (
        <div>
            <ol>
            <li><SiJavascript /></li>
            <li><FaPython /></li>
            <li><FaJava /></li>
            <li><FaHtml5 /></li>
            <li><FaCss3Alt /></li>
            <li><FaGitAlt /></li>
            <li><FaNode /></li>
            <li><FaReact /></li>
            <li><SiDjango /></li>
            <li><SiFlask /></li>
            <li><SiGraphql /></li>
            <li><SiSpring /></li>
            <li><FaJenkins /></li>
            <li><FaGitlab /></li>
            <li><SiKubernetes /></li>
            <li><FaDocker /></li>
            </ol>
        </div>
    )
}
