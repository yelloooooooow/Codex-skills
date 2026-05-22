function apply_publication_style(ax)
%APPLY_PUBLICATION_STYLE Apply a consistent figure style.
if nargin < 1 || isempty(ax), ax = gca; end
set(ax, "FontName", "Arial", "FontSize", 11, "LineWidth", 0.9, "Box", "on", "TickDir", "out");
grid(ax, "on");
ax.GridAlpha = 0.22;
fig = ancestor(ax, "figure");
if ~isempty(fig), set(fig, "Color", "w", "Renderer", "painters"); end
lines = findall(ax, "Type", "Line");
for k = 1:numel(lines)
    if lines(k).LineWidth < 1.5, lines(k).LineWidth = 1.5; end
end
end
