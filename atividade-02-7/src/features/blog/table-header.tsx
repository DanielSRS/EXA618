export function TableHeader() {
  return (
    <div
      style={{
        // border: "2px solid black",
        borderTop: 0,
        borderLeft: 0,
        borderRight: 0,
        padding: "2px",
        // borderRadius: "8px",
        display: "flex",
        flexDirection: "row",
        maxWidth: "600px",
        width: "100%",
        paddingBottom: "8px",
      }}
      className="line"
    >
      <p
        style={{
          flex: 1,
        }}
      >
        {"Author"}
      </p>
      <p
        style={{
          flex: 2,
        }}
      >
        {"Message"}
      </p>
      <div
        style={{
          display: "flex",
          flex: 1,
          flexDirection: "row",
          justifyContent: "space-between",
        }}
      >
        <span style={{ fontSize: "12px", color: "#666" }}>{"Date"}</span>
      </div>
    </div>
  );
}
