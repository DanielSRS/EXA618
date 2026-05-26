export function PostItem(props: {
  author: string;
  message: string;
  date: string;
}) {
  return (
    <div
      style={{
        border: "1px solid blue",
        padding: "16px",
        borderRadius: "8px",
        display: "flex",
        flexDirection: "column",
        maxWidth: "600px",
        width: "100%",
      }}
    >
      <p style={{}}>{props.message}</p>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          gap: "24px",
        }}
      >
        <p style={{}}>@{props.author}</p>
        <span style={{ fontSize: "12px", color: "#666" }}>
          {new Date(props.date).toLocaleString()}
        </span>
      </div>
    </div>
  );
}
