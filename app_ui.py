
"""
Elite Dangerous Advanced Analytics Platform
UI Structure - No Logic Implementation
Author: Data Science PhD Assistant
Python 3.12+ / PySide6

Run with: python elite_analytics_ui.py
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QLabel, QFrame, QSplitter, QTreeWidget, QTreeWidgetItem,
    QStackedWidget, QListWidget, QListWidgetItem, QGroupBox, QGridLayout,
    QProgressBar, QTableWidget, QTableWidgetItem, QHeaderView, QScrollArea,
    QSizePolicy, QSpacerItem
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor, QPalette, QIcon


class PlaceholderWidget(QFrame):
    """Placeholder widget for future chart/data implementations"""

    def __init__(self, title: str, description: str = "", height: int = 200):
        super().__init__()
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setMinimumHeight(height)
        self.setStyleSheet("""
            PlaceholderWidget {
                background-color: #1a1a2e;
                border: 1px solid #4a4a6a;
                border-radius: 8px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        title_label = QLabel(title)
        title_label.setFont(QFont("Segoe UI", 12, QFont.Bold))
        title_label.setStyleSheet("color: #00d4ff; background: transparent; border: none;")
        title_label.setAlignment(Qt.AlignCenter)

        desc_label = QLabel(description or "Chart/Data will be rendered here")
        desc_label.setStyleSheet("color: #888; background: transparent; border: none;")
        desc_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title_label)
        layout.addWidget(desc_label)


class StatusIndicator(QFrame):
    """Real-time status indicator widget"""

    def __init__(self, label: str, value: str = "---"):
        super().__init__()
        self.setStyleSheet("""
            StatusIndicator {
                background-color: #252540;
                border: 1px solid #3a3a5a;
                border-radius: 6px;
                padding: 8px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(4)

        self.label = QLabel(label)
        self.label.setStyleSheet("color: #888; font-size: 10px; background: transparent; border: none;")

        self.value = QLabel(value)
        self.value.setStyleSheet("color: #00ff88; font-size: 16px; font-weight: bold; background: transparent; border: none;")

        layout.addWidget(self.label)
        layout.addWidget(self.value)


class MetricCard(QFrame):
    """Card widget for displaying metrics"""

    def __init__(self, title: str, value: str, subtitle: str = "", color: str = "#00d4ff"):
        super().__init__()
        self.setFixedHeight(100)
        self.setStyleSheet(f"""
            MetricCard {{
                background-color: #1e1e3a;
                border-left: 4px solid {color};
                border-radius: 8px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)

        title_lbl = QLabel(title)
        title_lbl.setStyleSheet("color: #aaa; font-size: 11px; background: transparent; border: none;")

        value_lbl = QLabel(value)
        value_lbl.setStyleSheet(f"color: {color}; font-size: 24px; font-weight: bold; background: transparent; border: none;")

        subtitle_lbl = QLabel(subtitle)
        subtitle_lbl.setStyleSheet("color: #666; font-size: 10px; background: transparent; border: none;")

        layout.addWidget(title_lbl)
        layout.addWidget(value_lbl)
        layout.addWidget(subtitle_lbl)


# =============================================================================
# MAIN TAB CONTENT WIDGETS
# =============================================================================

class RealTimePanel(QWidget):
    """Real-Time monitoring panel - shows live game data"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Top status bar with live indicators
        status_row = QHBoxLayout()
        status_row.addWidget(StatusIndicator("GAME STATUS", "CONNECTED"))
        status_row.addWidget(StatusIndicator("CURRENT SHIP", "Alliance Chieftain"))
        status_row.addWidget(StatusIndicator("LOCATION", "Col 359 Sector CE-N b9-1"))
        status_row.addWidget(StatusIndicator("ACTIVITY", "Supercruise"))
        status_row.addWidget(StatusIndicator("SESSION TIME", "02:34:15"))
        layout.addLayout(status_row)

        # Main content splitter
        splitter = QSplitter(Qt.Horizontal)

        # Left: Live event feed
        left_panel = QFrame()
        left_panel.setStyleSheet("background-color: #12122a; border-radius: 8px;")
        left_layout = QVBoxLayout(left_panel)

        feed_label = QLabel("📡 LIVE EVENT FEED")
        feed_label.setStyleSheet("color: #00d4ff; font-weight: bold; padding: 10px;")
        left_layout.addWidget(feed_label)

        self.event_list = QListWidget()
        self.event_list.setStyleSheet("""
            QListWidget {
                background-color: #0a0a1a;
                border: none;
                color: #ccc;
                font-family: 'Consolas';
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #222;
            }
            QListWidget::item:hover {
                background-color: #1a1a3a;
            }
        """)
        # Sample events
        sample_events = [
            "🚀 [13:56:41] FSDJump → Col 359 Sector CE-N b9-1",
            "⚡ [13:56:32] NavRouteClear",
            "🔊 [13:55:51] Music → Supercruise",
            "🌟 [13:55:51] Scan → Star M8 (AutoScan)",
            "🎯 [13:55:41] FSDTarget → Col 359 Sector CE-N b9-1",
        ]
        for event in sample_events:
            self.event_list.addItem(event)
        left_layout.addWidget(self.event_list)

        splitter.addWidget(left_panel)

        # Right: Live charts
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)

        # Top row: Fuel and Cargo
        top_charts = QHBoxLayout()
        top_charts.addWidget(PlaceholderWidget("⛽ FUEL LEVEL", "Real-time fuel gauge", 150))
        top_charts.addWidget(PlaceholderWidget("📦 CARGO HOLD", "Cargo capacity visualization", 150))
        right_layout.addLayout(top_charts)

        # Middle: Session performance
        right_layout.addWidget(PlaceholderWidget("📈 SESSION PERFORMANCE", "Credits/hour, distance traveled, events/minute", 180))

        # Bottom: System map
        right_layout.addWidget(PlaceholderWidget("🗺️ CURRENT SYSTEM MAP", "3D visualization of current system bodies", 200))

        splitter.addWidget(right_panel)
        splitter.setSizes([350, 650])

        layout.addWidget(splitter)


class AnalysisPanel(QWidget):
    """General data analysis panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Metric cards row
        metrics_row = QHBoxLayout()
        metrics_row.addWidget(MetricCard("TOTAL WEALTH", "5.16B CR", "↑ 130M this session", "#00ff88"))
        metrics_row.addWidget(MetricCard("PLAY TIME", "554.7 hrs", "23.1 days total", "#00d4ff"))
        metrics_row.addWidget(MetricCard("SYSTEMS VISITED", "1,314", "↑ 31 this session", "#ff9f00"))
        metrics_row.addWidget(MetricCard("TRADE RANK", "TYCOON", "86% to Elite", "#bf00ff"))
        layout.addLayout(metrics_row)

        # Charts section
        charts_splitter = QSplitter(Qt.Horizontal)

        # Left column
        left_charts = QWidget()
        left_layout = QVBoxLayout(left_charts)
        left_layout.addWidget(PlaceholderWidget("💰 WEALTH PROGRESSION", "Historical credit accumulation over time", 200))
        left_layout.addWidget(PlaceholderWidget("📊 ACTIVITY BREAKDOWN", "Pie chart: Mining, Trading, Combat, Exploration", 200))

        charts_splitter.addWidget(left_charts)

        # Right column
        right_charts = QWidget()
        right_layout = QVBoxLayout(right_charts)
        right_layout.addWidget(PlaceholderWidget("🏆 RANK PROGRESSION", "All ranks over time with milestones", 200))
        right_layout.addWidget(PlaceholderWidget("🔧 ENGINEER PROGRESS", "Engineer unlock status and rank progress", 200))

        charts_splitter.addWidget(right_charts)

        layout.addWidget(charts_splitter)


class PredictionPanel(QWidget):
    """AI/ML prediction panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # AI Status header
        ai_status = QFrame()
        ai_status.setStyleSheet("background-color: #1a1a2e; border-radius: 8px; padding: 10px;")
        ai_layout = QHBoxLayout(ai_status)

        ai_icon = QLabel("🤖")
        ai_icon.setStyleSheet("font-size: 24px;")
        ai_layout.addWidget(ai_icon)

        ai_info = QVBoxLayout()
        ai_title = QLabel("AI PREDICTION ENGINE")
        ai_title.setStyleSheet("color: #00d4ff; font-weight: bold; font-size: 14px;")
        ai_subtitle = QLabel("Models: Prophet (Time Series) • Random Forest (Classification) • LSTM (Sequence)")
        ai_subtitle.setStyleSheet("color: #888; font-size: 11px;")
        ai_info.addWidget(ai_title)
        ai_info.addWidget(ai_subtitle)
        ai_layout.addLayout(ai_info)
        ai_layout.addStretch()

        model_status = QLabel("● Models Trained")
        model_status.setStyleSheet("color: #00ff88; font-weight: bold;")
        ai_layout.addWidget(model_status)

        layout.addWidget(ai_status)

        # Predictions grid
        grid = QGridLayout()
        grid.setSpacing(15)

        grid.addWidget(PlaceholderWidget("📈 ELITE TRADE PREDICTION", "Estimated days to Elite rank: 12.5 days", 180), 0, 0)
        grid.addWidget(PlaceholderWidget("💎 MINING YIELD FORECAST", "Next session estimated: 45M CR", 180), 0, 1)
        grid.addWidget(PlaceholderWidget("⚡ OPTIMAL PLAY TIMES", "Best efficiency hours based on history", 180), 1, 0)
        grid.addWidget(PlaceholderWidget("🎯 MATERIAL NEEDS", "Predicted engineering material shortages", 180), 1, 1)

        layout.addLayout(grid)

        # Forecast chart
        layout.addWidget(PlaceholderWidget("📊 30-DAY WEALTH FORECAST", "Prophet model prediction with confidence intervals", 200))


# =============================================================================
# SPECIALIZED TAB CONTENT WIDGETS
# =============================================================================

class MiningPanel(QWidget):
    """Mining (Asteroid) specialized panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Mining stats header
        stats_row = QHBoxLayout()
        stats_row.addWidget(MetricCard("TOTAL MINED", "9,731 units", "↑ 247 this session", "#ffd700"))
        stats_row.addWidget(MetricCard("MINING PROFIT", "2.79B CR", "All time earnings", "#00ff88"))
        stats_row.addWidget(MetricCard("BEST MINERAL", "Platinum", "Highest value mined", "#e5e4e2"))
        stats_row.addWidget(MetricCard("EFFICIENCY", "12.4M/hr", "Average rate", "#00d4ff"))
        layout.addLayout(stats_row)

        # Sub-tabs for mining
        mining_tabs = QTabWidget()
        mining_tabs.setStyleSheet(self._get_subtab_style())

        # Real-time mining tab
        realtime = QWidget()
        rt_layout = QVBoxLayout(realtime)
        rt_layout.addWidget(PlaceholderWidget("⛏️ LIVE PROSPECTOR RESULTS", "Current asteroid composition and content level", 150))

        rt_split = QHBoxLayout()
        rt_split.addWidget(PlaceholderWidget("🎯 ASTEROID SCANNER", "Visual representation of prospected asteroids", 200))
        rt_split.addWidget(PlaceholderWidget("📦 REFINERY STATUS", "Current bins and refinement progress", 200))
        rt_layout.addLayout(rt_split)

        mining_tabs.addTab(realtime, "⚡ Real-Time")

        # Analysis tab
        analysis = QWidget()
        an_layout = QVBoxLayout(analysis)
        an_layout.addWidget(PlaceholderWidget("📊 MINERAL DISTRIBUTION", "Breakdown of all minerals mined by type and value", 180))
        an_layout.addWidget(PlaceholderWidget("🗺️ HOTSPOT PERFORMANCE", "Mining locations ranked by efficiency", 180))

        mining_tabs.addTab(analysis, "📈 Analysis")

        # Prediction tab
        prediction = QWidget()
        pr_layout = QVBoxLayout(prediction)
        pr_layout.addWidget(PlaceholderWidget("🤖 YIELD PREDICTION", "ML model predicting next session yields", 180))
        pr_layout.addWidget(PlaceholderWidget("💰 MARKET TIMING", "Best times to sell based on market predictions", 180))

        mining_tabs.addTab(prediction, "🔮 Prediction")

        layout.addWidget(mining_tabs)

    def _get_subtab_style(self):
        return """
            QTabWidget::pane {
                border: 1px solid #3a3a5a;
                border-radius: 8px;
                background-color: #12122a;
            }
            QTabBar::tab {
                background-color: #1a1a2e;
                color: #888;
                padding: 8px 20px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background-color: #252550;
                color: #ffd700;
            }
            QTabBar::tab:hover:!selected {
                background-color: #202040;
            }
        """


class HaulingPanel(QWidget):
    """Trading/Hauling specialized panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Trading stats
        stats_row = QHBoxLayout()
        stats_row.addWidget(MetricCard("TRADE PROFIT", "6.47B CR", "All time market profits", "#00ff88"))
        stats_row.addWidget(MetricCard("COMMODITIES", "136,944", "Total units traded", "#00d4ff"))
        stats_row.addWidget(MetricCard("MARKETS", "18", "Unique markets visited", "#ff9f00"))
        stats_row.addWidget(MetricCard("BEST TRADE", "319.8M CR", "Single transaction record", "#bf00ff"))
        layout.addLayout(stats_row)

        # Sub-tabs
        hauling_tabs = QTabWidget()
        hauling_tabs.setStyleSheet(self._get_subtab_style())

        # Real-time
        realtime = QWidget()
        rt_layout = QVBoxLayout(realtime)
        rt_layout.addWidget(PlaceholderWidget("📦 CURRENT CARGO", "Live cargo hold contents and values", 150))
        rt_split = QHBoxLayout()
        rt_split.addWidget(PlaceholderWidget("🛒 MARKET PRICES", "Current station buy/sell prices", 200))
        rt_split.addWidget(PlaceholderWidget("🚚 TRADE ROUTE", "Active route with profit calculations", 200))
        rt_layout.addLayout(rt_split)
        hauling_tabs.addTab(realtime, "⚡ Real-Time")

        # Analysis
        analysis = QWidget()
        an_layout = QVBoxLayout(analysis)
        an_layout.addWidget(PlaceholderWidget("📈 PROFIT HISTORY", "Trade profit over time with trend lines", 180))
        an_layout.addWidget(PlaceholderWidget("🏪 TOP COMMODITIES", "Most profitable commodities traded", 180))
        hauling_tabs.addTab(analysis, "📈 Analysis")

        # Prediction
        prediction = QWidget()
        pr_layout = QVBoxLayout(prediction)
        pr_layout.addWidget(PlaceholderWidget("🤖 ROUTE OPTIMIZER", "AI-suggested optimal trade routes", 180))
        pr_layout.addWidget(PlaceholderWidget("📊 MARKET FORECAST", "Commodity price predictions (INARA data)", 180))
        hauling_tabs.addTab(prediction, "🔮 Prediction")

        # Fleet Carrier
        carrier = QWidget()
        fc_layout = QVBoxLayout(carrier)
        fc_layout.addWidget(PlaceholderWidget("🚢 CARRIER OVERVIEW", "Fleet Carrier: 3714237952 - Current location and status", 150))
        fc_split = QHBoxLayout()
        fc_split.addWidget(PlaceholderWidget("📥 IMPORT/EXPORT", "Carrier trade statistics", 180))
        fc_split.addWidget(PlaceholderWidget("⛽ TRITIUM TRACKER", "Fuel consumption and reserves", 180))
        fc_layout.addLayout(fc_split)
        hauling_tabs.addTab(carrier, "🚢 Fleet Carrier")

        layout.addWidget(hauling_tabs)

    def _get_subtab_style(self):
        return MiningPanel._get_subtab_style(self)


class CombatPanel(QWidget):
    """Combat specialized panel with sub-categories"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Combat stats
        stats_row = QHBoxLayout()
        stats_row.addWidget(MetricCard("BOUNTY PROFIT", "35.9M CR", "Total bounty earnings", "#ff4444"))
        stats_row.addWidget(MetricCard("BOUNTIES CLAIMED", "115", "Ships destroyed for bounty", "#ff9f00"))
        stats_row.addWidget(MetricCard("COMBAT RANK", "MOSTLY HARMLESS", "75% to next rank", "#00d4ff"))
        stats_row.addWidget(MetricCard("THARGOID ENCOUNTERS", "1", "Last: HIP 22557", "#00ff88"))
        layout.addLayout(stats_row)

        # Sub-tabs for combat types
        combat_tabs = QTabWidget()
        combat_tabs.setStyleSheet(self._get_subtab_style())

        # PVE Tab
        pve = QWidget()
        pve_layout = QVBoxLayout(pve)
        pve_layout.addWidget(PlaceholderWidget("🎯 BOUNTY HUNTING STATS", "NPC kills, profit per kill, favorite hunting grounds", 180))
        pve_layout.addWidget(PlaceholderWidget("⚔️ COMBAT ZONES", "Conflict zone participation history", 180))
        combat_tabs.addTab(pve, "👾 PVE (NPCs)")

        # PVP Tab
        pvp = QWidget()
        pvp_layout = QVBoxLayout(pvp)
        pvp_layout.addWidget(PlaceholderWidget("⚔️ PVP RECORD", "Player vs Player combat statistics", 180))
        pvp_layout.addWidget(PlaceholderWidget("🏆 POWERPLAY COMBAT", "Power-related combat activities", 180))
        combat_tabs.addTab(pvp, "🎮 PVP (Players)")

        # Thargoid Tab
        thargoid = QWidget()
        tg_layout = QVBoxLayout(thargoid)
        tg_layout.addWidget(PlaceholderWidget("👽 THARGOID ENCOUNTERS", "Encounter history and outcomes", 150))
        tg_split = QHBoxLayout()
        tg_split.addWidget(PlaceholderWidget("🔬 AX LOADOUT", "Current Anti-Xeno ship configuration", 180))
        tg_split.addWidget(PlaceholderWidget("🗺️ THREAT MAP", "Known Thargoid activity zones", 180))
        tg_layout.addLayout(tg_split)
        combat_tabs.addTab(thargoid, "👽 Thargoids")

        # Analysis/Prediction
        analysis = QWidget()
        an_layout = QVBoxLayout(analysis)
        an_layout.addWidget(PlaceholderWidget("📈 COMBAT EFFICIENCY", "Damage dealt, accuracy, survival rate", 180))
        an_layout.addWidget(PlaceholderWidget("🤖 THREAT PREDICTION", "AI analysis of dangerous systems", 180))
        combat_tabs.addTab(analysis, "📊 Analysis")

        layout.addWidget(combat_tabs)

    def _get_subtab_style(self):
        return MiningPanel._get_subtab_style(self)


class ColonizationPanel(QWidget):
    """System Colonization specialized panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Squadron/Colonization header
        header = QFrame()
        header.setStyleSheet("background-color: #1a1a2e; border-radius: 8px; padding: 15px;")
        header_layout = QHBoxLayout(header)

        squad_info = QVBoxLayout()
        squad_name = QLabel("🏛️ SYSTEM COLONIZATION")
        squad_name.setStyleSheet("color: #00d4ff; font-size: 18px; font-weight: bold;")
        squad_role = QLabel("Squadron Leader • ID: 109124")
        squad_role.setStyleSheet("color: #888; font-size: 12px;")
        squad_info.addWidget(squad_name)
        squad_info.addWidget(squad_role)
        header_layout.addLayout(squad_info)
        header_layout.addStretch()

        contrib = QVBoxLayout()
        contrib_label = QLabel("YOUR CONTRIBUTION")
        contrib_label.setStyleSheet("color: #888; font-size: 10px;")
        contrib_value = QLabel("89,872 pts")
        contrib_value.setStyleSheet("color: #00ff88; font-size: 20px; font-weight: bold;")
        contrib.addWidget(contrib_label)
        contrib.addWidget(contrib_value)
        header_layout.addLayout(contrib)

        layout.addWidget(header)

        # Stats row
        stats_row = QHBoxLayout()
        stats_row.addWidget(MetricCard("EXPLORATION", "68M pts", "Leaderboard contribution", "#00d4ff"))
        stats_row.addWidget(MetricCard("MINING", "1.26B pts", "Leaderboard contribution", "#ffd700"))
        stats_row.addWidget(MetricCard("BOUNTY", "348K pts", "Leaderboard contribution", "#ff4444"))
        stats_row.addWidget(MetricCard("COMBAT", "400 pts", "Leaderboard contribution", "#ff9f00"))
        layout.addLayout(stats_row)

        # Sub-tabs
        col_tabs = QTabWidget()
        col_tabs.setStyleSheet(self._get_subtab_style())

        # Active Projects
        projects = QWidget()
        pr_layout = QVBoxLayout(projects)
        pr_layout.addWidget(PlaceholderWidget("🏗️ ACTIVE COLONIZATION PROJECTS", "Current system colonization efforts and progress", 180))
        pr_layout.addWidget(PlaceholderWidget("📋 RESOURCE REQUIREMENTS", "Materials needed for current projects", 180))
        col_tabs.addTab(projects, "🏗️ Projects")

        # Leaderboards
        leaderboard = QWidget()
        lb_layout = QVBoxLayout(leaderboard)
        lb_layout.addWidget(PlaceholderWidget("🏆 SQUADRON LEADERBOARD", "Member rankings across all categories", 200))
        lb_layout.addWidget(PlaceholderWidget("📊 YOUR RANKINGS", "Your position in each category over time", 160))
        col_tabs.addTab(leaderboard, "🏆 Leaderboard")

        # Analysis
        analysis = QWidget()
        an_layout = QVBoxLayout(analysis)
        an_layout.addWidget(PlaceholderWidget("📈 CONTRIBUTION HISTORY", "Your colonization contributions over time", 180))
        an_layout.addWidget(PlaceholderWidget("🤖 PROJECT COMPLETION PREDICTION", "AI estimate for project completion dates", 180))
        col_tabs.addTab(analysis, "📈 Analysis")

        layout.addWidget(col_tabs)

    def _get_subtab_style(self):
        return MiningPanel._get_subtab_style(self)


class CommanderPanel(QWidget):
    """Commander, Ship, and System information panel"""

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)

        # Sub-tabs for Commander/Ship/System
        info_tabs = QTabWidget()
        info_tabs.setStyleSheet(self._get_subtab_style())

        # Commander Tab
        commander = QWidget()
        cmd_layout = QVBoxLayout(commander)

        # Commander header
        cmd_header = QFrame()
        cmd_header.setStyleSheet("background-color: #1a1a2e; border-radius: 8px; padding: 15px;")
        cmd_header_layout = QHBoxLayout(cmd_header)

        avatar = QLabel("👨‍🚀")
        avatar.setStyleSheet("font-size: 48px;")
        cmd_header_layout.addWidget(avatar)

        cmd_info = QVBoxLayout()
        cmd_name = QLabel("CMDR FILIPE79")
        cmd_name.setStyleSheet("color: #00d4ff; font-size: 20px; font-weight: bold;")
        cmd_id = QLabel("FID: F12543193")
        cmd_id.setStyleSheet("color: #888; font-size: 12px;")
        cmd_info.addWidget(cmd_name)
        cmd_info.addWidget(cmd_id)
        cmd_header_layout.addLayout(cmd_info)
        cmd_header_layout.addStretch()

        # Reputation summary
        rep_box = QVBoxLayout()
        rep_label = QLabel("FACTION REPUTATION")
        rep_label.setStyleSheet("color: #888; font-size: 10px;")
        rep_box.addWidget(rep_label)

        for faction, rep, color in [("Federation", "97%", "#00aaff"), ("Empire", "33%", "#ffaa00"), ("Alliance", "75%", "#00ff88")]:
            rep_row = QHBoxLayout()
            f_label = QLabel(faction)
            f_label.setStyleSheet(f"color: {color}; font-size: 11px;")
            r_label = QLabel(rep)
            r_label.setStyleSheet("color: #fff; font-size: 11px; font-weight: bold;")
            rep_row.addWidget(f_label)
            rep_row.addWidget(r_label)
            rep_box.addLayout(rep_row)

        cmd_header_layout.addLayout(rep_box)
        cmd_layout.addWidget(cmd_header)

        # Ranks
        cmd_layout.addWidget(PlaceholderWidget("🎖️ RANK PROGRESSION", "All ranks with progress bars: Combat, Trade, Explore, CQC, etc.", 150))

        # Materials
        cmd_layout.addWidget(PlaceholderWidget("🧪 MATERIALS INVENTORY", "Raw, Manufactured, Encoded materials with quantities", 180))

        info_tabs.addTab(commander, "👨‍🚀 Commander")

        # Ship Tab
        ship = QWidget()
        ship_layout = QVBoxLayout(ship)

        # Ship header
        ship_header = QFrame()
        ship_header.setStyleSheet("background-color: #1a1a2e; border-radius: 8px; padding: 15px;")
        ship_header_layout = QHBoxLayout(ship_header)

        ship_icon = QLabel("🚀")
        ship_icon.setStyleSheet("font-size: 48px;")
        ship_header_layout.addWidget(ship_icon)

        ship_info = QVBoxLayout()
        ship_name = QLabel("ALLIANCE CHIEFTAIN")
        ship_name.setStyleSheet("color: #00d4ff; font-size: 20px; font-weight: bold;")
        ship_id = QLabel("Ship ID: 34 • TypeX")
        ship_id.setStyleSheet("color: #888; font-size: 12px;")
        ship_info.addWidget(ship_name)
        ship_info.addWidget(ship_id)
        ship_header_layout.addLayout(ship_info)
        ship_header_layout.addStretch()

        # Quick stats
        quick_stats = QGridLayout()
        for i, (label, value) in enumerate([("Fuel", "14.5/16T"), ("Jump Range", "~25 LY"), ("Power", "24.9 MW")]):
            l = QLabel(label)
            l.setStyleSheet("color: #888; font-size: 10px;")
            v = QLabel(value)
            v.setStyleSheet("color: #00ff88; font-size: 14px; font-weight: bold;")
            quick_stats.addWidget(l, 0, i)
            quick_stats.addWidget(v, 1, i)
        ship_header_layout.addLayout(quick_stats)

        ship_layout.addWidget(ship_header)

        # Modules
        ship_layout.addWidget(PlaceholderWidget("⚙️ MODULE LOADOUT", "Current ship modules with power draw and priority", 200))

        # All ships
        ship_layout.addWidget(PlaceholderWidget("🚢 OWNED SHIPS", "All 5 owned ships with locations and values", 140))

        info_tabs.addTab(ship, "🚀 Ship")

        # System Tab
        system = QWidget()
        sys_layout = QVBoxLayout(system)

        sys_layout.addWidget(PlaceholderWidget("🌟 CURRENT SYSTEM", "Col 359 Sector CE-N b9-1 - System info and bodies", 150))
        sys_layout.addWidget(PlaceholderWidget("🗺️ GALAXY POSITION", "3D map showing current position in galaxy", 200))
        sys_layout.addWidget(PlaceholderWidget("📍 VISITED SYSTEMS", "Map of all 1,314 visited systems", 150))

        info_tabs.addTab(system, "🌌 System")

        # INARA Integration Tab
        inara = QWidget()
        inara_layout = QVBoxLayout(inara)

        inara_header = QFrame()
        inara_header.setStyleSheet("background-color: #1a1a2e; border-radius: 8px; padding: 15px;")
        ih_layout = QHBoxLayout(inara_header)

        inara_logo = QLabel("🌐 INARA")
        inara_logo.setStyleSheet("color: #00d4ff; font-size: 18px; font-weight: bold;")
        ih_layout.addWidget(inara_logo)
        ih_layout.addStretch()

        sync_status = QLabel("● Synced 5 min ago")
        sync_status.setStyleSheet("color: #00ff88;")
        ih_layout.addWidget(sync_status)

        inara_layout.addWidget(inara_header)
        inara_layout.addWidget(PlaceholderWidget("👤 INARA PROFILE", "Commander profile data from INARA API", 150))
        inara_layout.addWidget(PlaceholderWidget("📊 COMMUNITY DATA", "BGS data, market prices, and community goals", 200))

        info_tabs.addTab(inara, "🌐 INARA")

        layout.addWidget(info_tabs)

    def _get_subtab_style(self):
        return """
            QTabWidget::pane {
                border: 1px solid #3a3a5a;
                border-radius: 8px;
                background-color: #12122a;
            }
            QTabBar::tab {
                background-color: #1a1a2e;
                color: #888;
                padding: 10px 25px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background-color: #252550;
                color: #00d4ff;
            }
            QTabBar::tab:hover:!selected {
                background-color: #202040;
            }
        """


# =============================================================================
# MAIN WINDOW
# =============================================================================

class EliteAnalyticsMainWindow(QMainWindow):
    """Main application window with hierarchical navigation"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elite Dangerous Advanced Analytics Platform")
        self.setMinimumSize(1400, 900)
        self.setup_ui()
        self.apply_dark_theme()

    def setup_ui(self):
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Left navigation panel
        nav_panel = QFrame()
        nav_panel.setFixedWidth(220)
        nav_panel.setStyleSheet("""
            QFrame {
                background-color: #0d0d1a;
                border-right: 1px solid #2a2a4a;
            }
        """)
        nav_layout = QVBoxLayout(nav_panel)
        nav_layout.setContentsMargins(0, 0, 0, 0)
        nav_layout.setSpacing(0)

        # App header
        header = QFrame()
        header.setStyleSheet("background-color: #12122a; padding: 15px;")
        header_layout = QVBoxLayout(header)

        app_title = QLabel("ELITE ANALYTICS")
        app_title.setStyleSheet("color: #00d4ff; font-size: 16px; font-weight: bold; letter-spacing: 2px;")
        app_title.setAlignment(Qt.AlignCenter)

        app_subtitle = QLabel("Advanced Data Platform")
        app_subtitle.setStyleSheet("color: #666; font-size: 10px;")
        app_subtitle.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(app_title)
        header_layout.addWidget(app_subtitle)
        nav_layout.addWidget(header)

        # Navigation tree
        self.nav_tree = QTreeWidget()
        self.nav_tree.setHeaderHidden(True)
        self.nav_tree.setIndentation(20)
        self.nav_tree.setStyleSheet("""
            QTreeWidget {
                background-color: transparent;
                border: none;
                color: #aaa;
                font-size: 12px;
            }
            QTreeWidget::item {
                padding: 12px 15px;
                border-radius: 0;
            }
            QTreeWidget::item:hover {
                background-color: #1a1a3a;
            }
            QTreeWidget::item:selected {
                background-color: #252550;
                color: #00d4ff;
                border-left: 3px solid #00d4ff;
            }
            QTreeWidget::branch {
                background-color: transparent;
            }
        """)

        # Navigation structure
        nav_items = [
            ("🌐 GLOBAL", [
                ("⚡ Real-Time", "realtime"),
                ("📊 Analysis", "analysis"),
                ("🔮 Prediction", "prediction"),
            ]),
            ("⛏️ MINING", [
                ("Asteroid Mining", "mining"),
            ]),
            ("🚚 HAULING", [
                ("Trading & Cargo", "hauling"),
            ]),
            ("⚔️ COMBAT", [
                ("All Combat", "combat"),
            ]),
            ("🏛️ COLONIZATION", [
                ("System Colonization", "colonization"),
            ]),
            ("ℹ️ INFORMATION", [
                ("Commander/Ship/System", "commander"),
            ]),
        ]

        self.nav_mapping = {}

        for category, items in nav_items:
            cat_item = QTreeWidgetItem([category])
            cat_item.setFlags(cat_item.flags() & ~Qt.ItemIsSelectable)
            font = cat_item.font(0)
            font.setBold(True)
            font.setPointSize(9)
            cat_item.setFont(0, font)

            for name, key in items:
                child = QTreeWidgetItem([f"    {name}"])
                child.setData(0, Qt.UserRole, key)
                self.nav_mapping[key] = child
                cat_item.addChild(child)

            self.nav_tree.addTopLevelItem(cat_item)
            cat_item.setExpanded(True)

        nav_layout.addWidget(self.nav_tree)

        # Status footer
        footer = QFrame()
        footer.setStyleSheet("background-color: #12122a; padding: 10px;")
        footer_layout = QVBoxLayout(footer)

        status_indicator = QHBoxLayout()
        status_dot = QLabel("●")
        status_dot.setStyleSheet("color: #00ff88; font-size: 8px;")
        status_text = QLabel("Game Connected")
        status_text.setStyleSheet("color: #888; font-size: 10px;")
        status_indicator.addWidget(status_dot)
        status_indicator.addWidget(status_text)
        status_indicator.addStretch()

        footer_layout.addLayout(status_indicator)

        db_status = QLabel("PostgreSQL: Connected")
        db_status.setStyleSheet("color: #666; font-size: 9px;")
        footer_layout.addWidget(db_status)

        nav_layout.addWidget(footer)

        main_layout.addWidget(nav_panel)

        # Content area (stacked widget)
        self.content_stack = QStackedWidget()
        self.content_stack.setStyleSheet("background-color: #0a0a1a;")

        # Add all panels to stack
        self.panels = {
            "realtime": RealTimePanel(),
            "analysis": AnalysisPanel(),
            "prediction": PredictionPanel(),
            "mining": MiningPanel(),
            "hauling": HaulingPanel(),
            "combat": CombatPanel(),
            "colonization": ColonizationPanel(),
            "commander": CommanderPanel(),
        }

        for key, panel in self.panels.items():
            scroll = QScrollArea()
            scroll.setWidget(panel)
            scroll.setWidgetResizable(True)
            scroll.setStyleSheet("QScrollArea { border: none; background-color: #0a0a1a; }")
            self.content_stack.addWidget(scroll)

        main_layout.addWidget(self.content_stack)

        # Connect navigation
        self.nav_tree.itemClicked.connect(self.on_nav_clicked)

        # Select first item by default
        first_child = self.nav_tree.topLevelItem(0).child(0)
        self.nav_tree.setCurrentItem(first_child)
        self.content_stack.setCurrentIndex(0)

    def on_nav_clicked(self, item, column):
        key = item.data(0, Qt.UserRole)
        if key and key in self.panels:
            index = list(self.panels.keys()).index(key)
            self.content_stack.setCurrentIndex(index)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a1a;
            }
            QWidget {
                font-family: 'Segoe UI', sans-serif;
            }
            QScrollBar:vertical {
                background-color: #1a1a2e;
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background-color: #3a3a5a;
                border-radius: 5px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #4a4a7a;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar:horizontal {
                background-color: #1a1a2e;
                height: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:horizontal {
                background-color: #3a3a5a;
                border-radius: 5px;
                min-width: 30px;
            }
        """)


def main():
    app = QApplication(sys.argv)

    # Set application-wide font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    window = EliteAnalyticsMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
