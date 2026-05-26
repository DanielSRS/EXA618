import "./loading-indicator.css";

interface LoadingIndicatorProps {
  shown: boolean;
}

export function LoadingIndicator(props: LoadingIndicatorProps) {
  const isVisible = props.shown;

  if (!isVisible) {
    return null;
  }

  return (
    <div
      // className="spinner"
      style={{
        width: "40px",
        height: "40px",
        border: "4px solid #ccc",
        borderTop: "4px solid #333",
        borderRadius: "50%",
        animation: "spin 1s linear infinite",
      }}
    />
  );
}
