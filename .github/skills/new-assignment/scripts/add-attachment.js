const fs = require("fs");
const path = require("path");

const [id, name, file, type] = process.argv.slice(2);
const configPath = path.resolve(__dirname, "../../../../config.json");

if (!id || !name || !file || !type) {
  console.error(
    'Usage: node .github/skills/new-assignment/scripts/add-attachment.js <id> "<display-name>" <filename> <type>',
  );
  process.exit(1);
}

const config = JSON.parse(fs.readFileSync(configPath, "utf8"));
const assignment = config.assignments.find((item) => item.id === id);

if (!assignment) {
  console.error(`Assignment with id "${id}" was not found in config.json`);
  process.exit(1);
}

if (!assignment.attachments) {
  assignment.attachments = [];
}

assignment.attachments.push({
  name,
  file,
  type,
});

fs.writeFileSync(configPath, JSON.stringify(config, null, 2) + "\n");
console.log(`Added attachment "${name}" for "${id}"`);
