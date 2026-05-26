"use client";
import { useEffect, useMemo, useState } from "react";
import { LoadingIndicator } from "./loading-indicator";
import { PostItem } from "./post-item";
import { SearchBox } from "./search-box";
import { TableHeader } from "./table-header";

const POSTS_URL =
  "https://script.google.com/macros/s/AKfycbzBn3sALe1rYjz7Ze-Ik7q9TEVP0I2V3XX7GNcecWP8NvCzGt4yO_RT1OlQp09TE9cU/exec";

async function getPosts() {
  const res = fetch(POSTS_URL);
  return res
    .then((response) => response.json())
    .then((data) => {
      console.log("Data", data);
      return data as [string, string, string][];
    })
    .catch((err) => {
      console.log("Error", err);
      return [] as [string, string, string][];
    });
}

export function SearchPosts() {
  const [posts, setPosts] = useState<[string, string, string][] | undefined>();
  const [searchTerm, setSearchTerm] = useState("");
  const filteredPosts = useMemo(() => {
    if (!searchTerm) return posts;
    return posts?.filter((data) => {
      const [message, author] = data;
      return (
        message.toString().toLowerCase().includes(searchTerm.toLowerCase()) ||
        author.toString().toLowerCase().includes(searchTerm.toLowerCase())
      );
    });
  }, [searchTerm, posts]);

  useEffect(() => {
    getPosts().then(setPosts);
  }, []);

  const isLoading = posts === undefined;
  // const isLoading = true;
  return (
    <div
      className="flex flex-col"
      style={{
        // border: "1px solid red",
        flex: 1,
        maxHeight: "100vh",
      }}
    >
      {/* Header */}
      <Header>
        {/* Search box */}
        <SearchBox onSearch={setSearchTerm} />
      </Header>
      {/* Posts area */}
      <PostsContainer isLoading={isLoading}>
        {/* Posts will be rendered here */}
        {!isLoading && <TableHeader />}
        {!isLoading &&
          filteredPosts?.map(([message, author, date], index) => (
            <PostItem
              key={index}
              author={author}
              message={message}
              date={date}
            />
          ))}
        <LoadingIndicator shown={isLoading} />
      </PostsContainer>
    </div>
  );
}

function Header(props: { children: React.ReactNode }) {
  return (
    <div
      style={{
        // border: "1px solid green",
        width: "100%",
        // height: "76px",
        justifyContent: "center",
        alignItems: "center",
        display: "flex",
        // flexDirection: "column",
        paddingTop: "16px",
        paddingBottom: "8px",
      }}
    >
      {props.children}
    </div>
  );
}

function PostsContainer(props: {
  children: React.ReactNode;
  isLoading: boolean;
}) {
  return (
    <div
      className="line"
      style={{
        // border: "3px solid orange",
        borderTop: "2px solid #000",
        flex: 1,
        display: "flex",
        flexDirection: "column",
        justifyContent: props.isLoading ? "center" : undefined,
        alignItems: "center",
        scrollBehavior: "smooth",
        overflowY: "scroll",
        padding: "16px",
        gap: "8px",
      }}
    >
      {props.children}
    </div>
  );
}
