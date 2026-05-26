interface SearchBoxProps {
  onSearch: (searchTerm: string) => void;
}

export function SearchBox(props: SearchBoxProps) {
  return (
    <input
      type="text"
      className="line"
      style={{
        minHeight: "40x",
        minWidth: "250px",
        border: "2px solid blue",
        padding: "8px",
        paddingLeft: "16px",
        paddingRight: "16px",
        borderRadius: "8px",
      }}
      onChange={(e) => props.onSearch(e.target.value ?? "")}
      placeholder="Search.."
    />
  );
}
