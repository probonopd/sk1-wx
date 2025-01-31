# -*- coding: utf-8 -*-
#
#  Copyright (C) 2013 by Igor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import wal

ICON_SIZES = [16, 22, 24, 32, 48, 64, 128]

PD_NEW = 'gtk-new'
PD_OPEN = 'gtk-open'
PD_FILE_SAVE = 'gtk-save'
PD_FILE_SAVE_AS = 'gtk-save-as'
PD_CLOSE = 'gtk-close'
PD_PRINT_PREVIEW = 'gtk-print-preview'
PD_PRINT = 'gtk-print'
PD_QUIT = 'gtk-quit'
PD_UNDO = 'gtk-undo'
PD_REDO = 'gtk-redo'
PD_CUT = 'gtk-cut'
PD_COPY = 'gtk-copy'
PD_PASTE = 'gtk-paste'
PD_DELETE = 'gtk-delete'
PD_EDIT = 'gtk-edit'
PD_SELECTALL = 'gtk-select-all'
PD_PROPERTIES = 'gtk-properties'
PD_PREFERENCES = 'gtk-preferences'
PD_ZOOM = 'zoom'
PD_ZOOM_100 = 'gtk-zoom-100'
PD_ZOOM_IN = 'gtk-zoom-in'
PD_ZOOM_OUT = 'gtk-zoom-out'
PD_ZOOM_PAGE = 'gtk-zoom-page'
PD_ZOOM_FIT = 'gtk-zoom-fit'
PD_REFRESH = 'gtk-refresh'
PD_INSERT_PAGE = 'action-insert-page'
PD_DELETE_PAGE = 'action-delete-page'
PD_GOTO_PAGE = 'action-goto-page'
PD_NEXT_PAGE = 'action-next-page'
PD_PREV_PAGE = 'action-previous-page'
PD_GUIDES_AT_CENTER = 'action-guides-at-center'
PD_PAGE_FRAME = 'action-page-frame'
PD_PAGE_GUIDE_FRAME = 'action-page-guide-frame'
PD_REMOVE_ALL_GUIDES = 'action-remove-all-guides'
PD_TO_CURVES = 'action-to-curves'
PD_COMBINE = 'action-combine'
PD_BREAK = 'action-break'
PD_RAISE_TO_TOP = 'action-raise-to-top'
PD_RAISE = 'action-raise'
PD_LOWER = 'action-lower'
PD_LOWER_TO_BOTTOM = 'action-lower-to-bottom'
PD_GROUP = 'action-group'
PD_UNGROUP = 'action-ungroup'
PD_UNGROUP_ALL = 'action-ungroup-all'

PD_CONV_TO_CMYK = 'action-to-cmyk'
PD_CONV_TO_RGB = 'action-to-rgb'
PD_CONV_TO_LAB = 'action-to-lab'
PD_CONV_TO_GRAY = 'action-to-gray'
PD_CONV_TO_BW = 'action-to-bw'
PD_CONV_TO_SPOT = 'action-to-spot'
PD_EMPTY = 'action-empty'
PD_EVENODD = 'action-evenodd'
PD_NONZERO = 'action-nonzero'
PD_FILL_ANY = 'action-fill-any'
PD_FILL_CLOSED_ONLY = 'action-fill-closed-only'
PD_INVERT_BITMAP = 'action-invert-bitmap'

PD_TOOL_PAGES = 'pdesign-tool-pages'
PD_TOOL_LAYERS = 'pdesign-tool-layers'
PD_TOOL_OBJBROWSER = 'pdesign-tool-objbrowser'

PD_WARNING = 'gtk-dialog-warning'
PD_HOME = 'gtk-home'
PD_FBPAGE = 'sk1-fb'
PD_ABOUT = 'gtk-about'
PD_STUB_NEW = 'stub-new'
PD_STUB_OPEN = 'stub-open'
PD_STUB_RECENT = 'stub-recent'

L_ORIGIN_CENTER = 'doc-origin-center'
L_ORIGIN_LL = 'doc-origin-ll'
L_ORIGIN_LU = 'doc-origin-lu'

PD_CLOSE_BUTTON = 'pdesign-close-button'
PD_CLOSE_BUTTON_ACTIVE = 'pdesign-close-button-active'
PD_MOUSE_MONITOR = 'mouse-monitor'
PD_APP_STATUS = 'app-status'
PD_PM_ARROW_END = "pager-arrow-end"
PD_PM_ARROW_LEFT = "pager-arrow-left"
PD_PM_ARROW_RIGHT = "pager-arrow-right"
PD_PM_ARROW_START = "pager-arrow-start"

PD_SNAP_TO_GRID_OFF = 'snap-to-grid-off'
PD_SNAP_TO_GRID_ON = 'snap-to-grid-on'
PD_SNAP_TO_GUIDE_OFF = 'snap-to-guide-off'
PD_SNAP_TO_GUIDE_ON = 'snap-to-guide-on'
PD_SNAP_TO_OBJ_OFF = 'snap-to-obj-off'
PD_SNAP_TO_OBJ_ON = 'snap-to-obj-on'
PD_SNAP_TO_PAGE_OFF = 'snap-to-page-off'
PD_SNAP_TO_PAGE_ON = 'snap-to-page-on'

PD_PREFS_CMS = 'prefs-cms'
PD_PREFS_CMS_BANNER = 'prefs-cms-banner'
PD_PREFS_PALETTE = 'prefs-palette'
PD_PREFS_RULER = 'prefs-ruler'
PD_PREFS_GRID = 'prefs-grid'
PD_PREFS_PRINTERS = 'prefs-printers'
PD_NO_PRINTERS = 'prefs-no-printers'

PD_PALETTE_AUTO = 'palette-auto'
PD_PALETTE_LARGE = 'palette-large'
PD_PALETTE_LIST = 'palette-list'
PD_PALETTE_NORMAL = 'palette-normal'
PD_PALETTE_SWATCH = 'palette-swatch'
PD_DOWNLOAD48 = 'download-48'
PD_LARGE_SEL_PALETTE = 'large-cell-selection'
PD_SMALL_SEL_PALETTE = 'small-cell-selection'

PD_CAP_BUTT = 'cap-butt'
PD_CAP_SQUARE = 'cap-projecting'
PD_CAP_ROUND = 'cap-round'
PD_JOIN_BEVEL = 'join-bevel'
PD_JOIN_MITER = 'join-miter'
PD_JOIN_ROUND = 'join-round'

PD_LINEAR_GRAD = 'linear-grad'
PD_RADIAL_GRAD = 'radial-grad'

PD_GOTO_FIRST = 'gtk-goto-first'
PD_GO_BACK = 'gtk-go-back'
PD_GO_FORWARD = 'gtk-go-forward'
PD_GOTO_LAST = 'gtk-goto-last'

PD_ADD = 'gtk-add'
PD_REMOVE = 'gtk-remove'

PD_BEZIER_SEL_ALL_NODES = 'bezier-sel-all-nodes'
PD_BEZIER_REVERSE_ALL_PATHS = 'bezier-reverse-all-paths'
PD_BEZIER_SEL_SUBPATH_NODES = 'bezier-sel-subpath-nodes'
PD_BEZIER_DEL_SUBPATH = 'bezier-del-subpath'
PD_BEZIER_REVERSE_SUBPATH = 'bezier-reverse-subpath'
PD_BEZIER_EXTRACT_SUBPATH = 'bezier-extract-subpath'
PD_BEZIER_ADD_NODE = 'bezier-add-node'
PD_BEZIER_DELETE_NODE = 'bezier-delete-node'
PD_BEZIER_ADD_SEG = 'bezier-add-seg'
PD_BEZIER_DELETE_SEG = 'bezier-del-seg'
PD_BEZIER_JOIN_NODE = 'bezier-join-node'
PD_BEZIER_SPLIT_NODE = 'bezier-split-node'
PD_BEZIER_SEG_TO_LINE = 'bezier-to-line'
PD_BEZIER_SEG_TO_CURVE = 'bezier-to-curve'
PD_BEZIER_NODE_CUSP = 'bezier-cusp'
PD_BEZIER_NODE_SMOOTH = 'bezier-smooth'
PD_BEZIER_NODE_SYMMETRICAL = 'bezier-symmetric'

PD_PATTERN_ORIGIN_X = 'pattern-origin-x'
PD_PATTERN_ORIGIN_Y = 'pattern-origin-y'
PD_PATTERN_ROTATE = 'pattern-rotate'
PD_PATTERN_SCALE_X = 'pattern-scale-x'
PD_PATTERN_SCALE_Y = 'pattern-scale-y'
PD_PATTERN_SHEAR_X = 'pattern-shear-x'
PD_PATTERN_SHEAR_Y = 'pattern-shear-y'

PD_POSITION_PLGN = 'transform-position'
PD_RESIZE_PLGN = 'transform-resize'
PD_SCALE_PLGN = 'transform-scale'
PD_ROTATE_PLGN = 'transform-rotate'
PD_SHEAR_PLGN = 'transform-shear'

PD_PATHS_EXCLUSION = 'paths-exclusion'
PD_PATHS_FUSION = 'paths-fusion'
PD_PATHS_INTERSECTION = 'paths-intersection'
PD_PATHS_TRIM = 'paths-trim'

PD_LAYER_NEW = 'action-layer-new'
PD_LAYER_DELETE = 'action-layer-delete'

PD_ALIGN_LEFT = 'align-left'
PD_ALIGN_CENTER = 'align-center'
PD_ALIGN_RIGHT = 'align-right'
PD_ALIGN_JUSTIFY = 'align-justify'
PD_LIGATURE = 'ctx-ligature'

PD_FONT = 'ctx-font'

PD_TEXT_BOLD = 'text-bold'
PD_TEXT_ITALIC = 'text-italic'
PD_TEXT_STRIKETHROUGH = 'text-strikethrough'
PD_TEXT_SUBSCRIPT = 'text-subscript'
PD_TEXT_SUPERSCRIPT = 'text-superscript'
PD_TEXT_UNDERLINE = 'text-underline'
PD_TEXT_CAPITALIZE = 'text-capitalize'
PD_TEXT_LOWERCASE = 'text-lowercase'
PD_TEXT_UPPERCASE = 'text-uppercase'
PD_TEXT_CLEAR_MARKUP = 'text-clear-markup'

PD_PLUGIN_ICONIZER = 'plugin-iconizer'

PD_PRINT_COPIES_00 = 'print-copies'
PD_PRINT_COPIES_10 = 'print-copies-col'
PD_PRINT_COPIES_01 = 'print-copies-rev'
PD_PRINT_COPIES_11 = 'print-copies-rev-col'

PD_PRINTER_LASER = 'printer-laser'
PD_PRINTER_INKJET = 'printer-inkjet'
PD_PRINTER_PDF = 'printer-pdf'

PD_PRINTMODE_MONO = 'print-mode-mono'
PD_PRINTMODE_COLOR = 'print-mode-color'

PD_PRINTORIENT_PORTRAIT = 'print-orient-portrait'
PD_PRINTORIENT_LANDSCAPE = 'print-orient-landscape'

# ----- MacOS X specific bitmaps
MAC_TBB_NORMAL = 'tbb-normal'
MAC_TBB_PRESSED = 'tbb-pressed'
MAC_TBNB_LEFT_NORMAL = 'tbnb-left-normal'
MAC_TBNB_LEFT_PRESSED = 'tbnb-left-pressed'
MAC_TBNB_MIDDLE_NORMAL = 'tbnb-middle-normal'
MAC_TBNB_MIDDLE_PRESSED = 'tbnb-middle-pressed'
MAC_TBNB_RIGHT_NORMAL = 'tbnb-right-normal'
MAC_TBNB_RIGHT_PRESSED = 'tbnb-right-pressed'
MAC_TBNB_SPACER_ACTIVE = 'tbnb-spacer-active'
MAC_TBNB_SPACER_NORMAL = 'tbnb-spacer-normal'

ICON_MATCH = {
    wal.ART_NEW: PD_NEW,
    wal.ART_FILE_OPEN: PD_OPEN,
    wal.ART_FILE_SAVE: PD_FILE_SAVE,
    wal.ART_FILE_SAVE_AS: PD_FILE_SAVE_AS,
    wal.ART_PRINT: PD_PRINT,
    wal.ART_QUIT: PD_QUIT,
    wal.ART_UNDO: PD_UNDO,
    wal.ART_REDO: PD_REDO,
    wal.ART_CUT: PD_CUT,
    wal.ART_COPY: PD_COPY,
    wal.ART_PASTE: PD_PASTE,
    wal.ART_DELETE: PD_DELETE,
    wal.ART_WARNING: PD_WARNING,
}

SK1_ICON16 = 'sk1-icon-16x16'
SK1_ICON22 = 'sk1-icon-22x22'
SK1_ICON32 = 'sk1-icon-32x32'
SK1_ICON48 = 'sk1-icon-48x48'
SK1_ICON64 = 'sk1-icon-64x64'
SK1_ICON128 = 'sk1-icon-128x128'
CAIRO_BANNER = 'cairo-banner'
DOCUMENT_ICON = 'document-icon'
PLUGIN_ICON = 'plugin-icon'
ARROW_LEFT = 'arrow-left'
ARROW_RIGHT = 'arrow-right'
ARROW_TOP = 'arrow-top'
ARROW_BOTTOM = 'arrow-bottom'
DOUBLE_ARROW_LEFT = 'double-arrow-left'
DOUBLE_ARROW_RIGHT = 'double-arrow-right'
NO_COLOR = 'no-color'
SLIDER_KNOB = 'slider-knob'
SLIDER_STOP = 'slider-stop'
SLIDER_KNOB_SEL = 'slider-knob-selected'
SLIDER_STOP_SEL = 'slider-stop-selected'
REG_SIGN = 'reg-sign'
POPUP_MENU = 'popup-menu'

GENERICS = [SK1_ICON16, SK1_ICON22, SK1_ICON32, SK1_ICON48, SK1_ICON64,
            SK1_ICON128,
            CAIRO_BANNER, DOCUMENT_ICON, ARROW_LEFT, ARROW_RIGHT, PLUGIN_ICON,
            ARROW_TOP, ARROW_BOTTOM, SLIDER_KNOB, REG_SIGN,
            PD_LARGE_SEL_PALETTE,
            PD_SMALL_SEL_PALETTE, PD_CAP_BUTT, PD_CAP_SQUARE, PD_CAP_ROUND,
            PD_JOIN_BEVEL, PD_JOIN_MITER, PD_JOIN_ROUND, PD_LINEAR_GRAD,
            PD_RADIAL_GRAD,
            SLIDER_STOP, SLIDER_KNOB_SEL, SLIDER_STOP_SEL, POPUP_MENU,
            DOUBLE_ARROW_LEFT, DOUBLE_ARROW_RIGHT, NO_COLOR, PD_TO_CURVES,
            PD_GROUP, PD_UNGROUP, PD_UNGROUP_ALL, PD_COMBINE, PD_BREAK,
            PD_TOOL_PAGES, PD_TOOL_LAYERS, PD_TOOL_OBJBROWSER, PD_FBPAGE,
            PD_CLOSE_BUTTON, PD_CLOSE_BUTTON_ACTIVE,
            L_ORIGIN_CENTER, L_ORIGIN_LL, L_ORIGIN_LU,
            PD_MOUSE_MONITOR, PD_PM_ARROW_END, PD_PM_ARROW_LEFT,
            PD_PM_ARROW_RIGHT, PD_PM_ARROW_START, PD_APP_STATUS,
            PD_GUIDES_AT_CENTER,
            PD_INSERT_PAGE, PD_DELETE_PAGE, PD_GOTO_PAGE, PD_NEXT_PAGE,
            PD_PREV_PAGE, PD_ZOOM,
            PD_PAGE_FRAME, PD_PAGE_GUIDE_FRAME, PD_REMOVE_ALL_GUIDES,
            PD_RAISE_TO_TOP, PD_RAISE, PD_LOWER, PD_LOWER_TO_BOTTOM,
            PD_STUB_NEW, PD_STUB_OPEN, PD_STUB_RECENT, PD_CONV_TO_CMYK,
            PD_CONV_TO_RGB, PD_CONV_TO_LAB, PD_CONV_TO_GRAY, PD_CONV_TO_BW,
            PD_CONV_TO_SPOT, PD_EMPTY, PD_EVENODD, PD_NONZERO, PD_FILL_ANY,
            PD_FILL_CLOSED_ONLY, PD_PATTERN_ORIGIN_X, PD_PATTERN_ORIGIN_Y,
            PD_PATTERN_ROTATE, PD_PATTERN_SCALE_X, PD_PATTERN_SCALE_Y,
            PD_PATTERN_SHEAR_X, PD_PATTERN_SHEAR_Y, PD_PATHS_TRIM,
            PD_PATHS_INTERSECTION, PD_PATHS_EXCLUSION, PD_PATHS_FUSION,
            PD_POSITION_PLGN, PD_RESIZE_PLGN, PD_SCALE_PLGN, PD_ROTATE_PLGN,
            PD_SHEAR_PLGN,
            PD_INVERT_BITMAP, PD_SNAP_TO_GRID_OFF, PD_SNAP_TO_GRID_ON,
            PD_SNAP_TO_GUIDE_OFF, PD_SNAP_TO_GUIDE_ON, PD_SNAP_TO_OBJ_OFF,
            PD_SNAP_TO_OBJ_ON, PD_SNAP_TO_PAGE_OFF, PD_SNAP_TO_PAGE_ON,
            PD_BEZIER_ADD_NODE, PD_BEZIER_DELETE_NODE, PD_BEZIER_ADD_SEG,
            PD_BEZIER_DELETE_SEG, PD_BEZIER_JOIN_NODE, PD_BEZIER_SPLIT_NODE,
            PD_BEZIER_SEG_TO_LINE, PD_BEZIER_SEG_TO_CURVE, PD_BEZIER_NODE_CUSP,
            PD_BEZIER_NODE_SMOOTH, PD_BEZIER_NODE_SYMMETRICAL,
            PD_BEZIER_SEL_ALL_NODES,
            PD_BEZIER_REVERSE_ALL_PATHS, PD_BEZIER_SEL_SUBPATH_NODES,
            PD_BEZIER_DEL_SUBPATH, PD_BEZIER_REVERSE_SUBPATH,
            PD_BEZIER_EXTRACT_SUBPATH,
            PD_LAYER_NEW, PD_LAYER_DELETE, PD_ALIGN_LEFT, PD_ALIGN_CENTER,
            PD_ALIGN_RIGHT, PD_ALIGN_JUSTIFY, PD_LIGATURE, PD_FONT,
            PD_TEXT_BOLD, PD_TEXT_ITALIC, PD_TEXT_STRIKETHROUGH,
            PD_TEXT_SUBSCRIPT,
            PD_TEXT_SUPERSCRIPT, PD_TEXT_UNDERLINE, PD_TEXT_CAPITALIZE,
            PD_TEXT_LOWERCASE, PD_TEXT_UPPERCASE, PD_TEXT_CLEAR_MARKUP,
            PD_PRINT_COPIES_00, PD_PRINT_COPIES_10, PD_PRINT_COPIES_01,
            PD_PRINT_COPIES_11,
            PD_PRINTER_LASER, PD_PRINTER_INKJET, PD_PRINTMODE_MONO,
            PD_PRINTMODE_COLOR,
            PD_PRINTORIENT_PORTRAIT, PD_PRINTORIENT_LANDSCAPE, PD_PRINTER_PDF,

            PD_PREFS_CMS, PD_PREFS_PALETTE, PD_PREFS_RULER, PD_PREFS_GRID,
            PD_PREFS_CMS_BANNER, PD_PREFS_PRINTERS, PD_NO_PRINTERS,

            PD_PALETTE_AUTO, PD_PALETTE_LARGE, PD_PALETTE_LIST,
            PD_PALETTE_NORMAL, PD_PALETTE_SWATCH,

            PD_PLUGIN_ICONIZER,

            PD_DOWNLOAD48, ]

TOOL_CREATE_CURVE = 'tool-create-curve'
TOOL_CREATE_ELLIPSE = 'tool-create-ellipse'
TOOL_CREATE_POLY = 'tool-create-poly'
TOOL_CREATE_POLYGON = 'tool-create-polygon'
TOOL_CREATE_RECT = 'tool-create-rect'
TOOL_CREATE_TEXT = 'tool-create-text'
TOOL_FILL = 'tool-fill'
TOOL_FLEUR = 'tool-fleur'
TOOL_GRADIENT = 'tool-gradient'
TOOL_SELECT = 'tool-select'
TOOL_SHAPER = 'tool-shaper'
TOOL_STROKE = 'tool-stroke'
TOOL_ZOOM = 'tool-zoom'

TOOLS_ICONS = [TOOL_CREATE_CURVE, TOOL_CREATE_ELLIPSE, TOOL_CREATE_POLY,
               TOOL_CREATE_POLYGON, TOOL_CREATE_RECT, TOOL_CREATE_TEXT,
               TOOL_FILL,
               TOOL_FLEUR, TOOL_GRADIENT, TOOL_SELECT, TOOL_SHAPER, TOOL_STROKE,
               TOOL_ZOOM, ]

CTX_PAGE_LANDSCAPE = 'ctx-page-landscape'
CTX_PAGE_PORTRAIT = 'ctx-page-portrait'
CTX_UNITS = 'ctx-units'
CTX_OBJECT_JUMP = 'ctx-object-jump'
CTX_OBJECT_RESIZE = 'ctx-object-resize'
CTX_RATIO = 'ctx-ratio'
CTX_NO_RATIO = 'ctx-no-ratio'
CTX_W_ON_H = 'ctx-w-on-h'
CTX_ROTATE = 'ctx-rotate'
CTX_ROTATE_LEFT = 'ctx-rotate-left'
CTX_ROTATE_RIGHT = 'ctx-rotate-right'
CTX_MIRROR_H = 'ctx-mirror-h'
CTX_MIRROR_V = 'ctx-mirror-v'
CTX_POLYGON_NUM = 'ctx-plgn-num'
CTX_POLYGON_CFG = 'ctx-plgn-cfg'
CTX_ROUNDED_RECT = 'ctx-rounded-rect'
CTX_ROUNDED_RECT1_ON = 'ctx-rounded-rect1_on'
CTX_ROUNDED_RECT1_OFF = 'ctx-rounded-rect1_off'
CTX_ROUNDED_RECT2_ON = 'ctx-rounded-rect2_on'
CTX_ROUNDED_RECT2_OFF = 'ctx-rounded-rect2_off'
CTX_ROUNDED_RECT3_ON = 'ctx-rounded-rect3_on'
CTX_ROUNDED_RECT3_OFF = 'ctx-rounded-rect3_off'
CTX_ROUNDED_RECT4_ON = 'ctx-rounded-rect4_on'
CTX_ROUNDED_RECT4_OFF = 'ctx-rounded-rect4_off'
CTX_CIRCLE_ARC = 'circle-arc'
CTX_CIRCLE_CHORD = 'circle-chord'
CTX_CIRCLE_PIE_SLICE = 'circle-pie-slice'
CTX_CIRCLE_END_ANGLE = 'ctx-circle-end-angle'
CTX_CIRCLE_START_ANGLE = 'ctx-circle-start-angle'

CTX_ICONS = [CTX_PAGE_LANDSCAPE, CTX_PAGE_PORTRAIT, CTX_UNITS, CTX_OBJECT_JUMP,
             CTX_OBJECT_RESIZE, CTX_RATIO, CTX_NO_RATIO, CTX_W_ON_H, CTX_ROTATE,
             CTX_ROTATE_LEFT, CTX_ROTATE_RIGHT, CTX_MIRROR_H, CTX_MIRROR_V,
             CTX_POLYGON_NUM, CTX_POLYGON_CFG, CTX_ROUNDED_RECT,
             CTX_ROUNDED_RECT1_ON, CTX_ROUNDED_RECT1_OFF, CTX_ROUNDED_RECT2_ON,
             CTX_ROUNDED_RECT2_OFF, CTX_ROUNDED_RECT3_ON, CTX_ROUNDED_RECT3_OFF,
             CTX_ROUNDED_RECT4_ON, CTX_ROUNDED_RECT4_OFF, CTX_CIRCLE_ARC,
             CTX_CIRCLE_CHORD, CTX_CIRCLE_PIE_SLICE, CTX_CIRCLE_END_ANGLE,
             CTX_CIRCLE_START_ANGLE, ]

GENERIC_ICONS = TOOLS_ICONS + GENERICS + CTX_ICONS
