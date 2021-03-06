// Entry point for the unpkg bundle containing custom model definitions.
//
// It differs from the notebook bundle in that it does not need to define a
// dynamic baseURL for the static assets and may load some css that would
// already be loaded by the notebook otherwise.

// Export the npm package version number
export const version = require("../package.json").version;

// Export widget models and views
export * from "./datawidgets";
export * from "./plotwidgets";
