export function PostItem(props: {
  author: string;
  message: string;
  date: string;
}) {
  return (
    <div
      style={{
        border: "2px solid black",
        padding: "16px",
        // borderRadius: "8px",
        display: "flex",
        flexDirection: "column",
        maxWidth: "600px",
        width: "100%",
      }}
      className="line"
    >
      <p style={{}}>{props.message}</p>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
        }}
      >
        <p style={{}}>@{props.author}</p>
        <span style={{ fontSize: "12px", color: "#666" }}>
          {new Date(props.date).toLocaleString("pt-br")}
        </span>
      </div>
    </div>
  );
}
