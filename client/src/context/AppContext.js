import React, { createContext, useState} from 'react';
export const AppContext = createContext();

export const AppContextProvider = ({ children }) => {
  const [contextMessage, setContextMessage] = useState('');
  const [projects, setProjects] = useState([]);
  const [blogs, setBlogs] = useState([]);
  const contextMethod = () => {
    setContextMessage('Hello from client/src/context/AppContext.jsx');
  };

  return (
    <AppContext.Provider
      value={{
        contextMessage,
        contextMethod,
        projects, 
        setProjects,
        blogs, 
        setBlogs
      }}
    >
      {children}
    </AppContext.Provider>
  );
};